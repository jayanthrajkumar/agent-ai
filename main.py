"""
AI Research Agent

This script builds an AI-powered research assistant using LangChain and Groq LLaMA 3.1.
The agent can:
- Search the web
- Retrieve Wikipedia information
- Generate structured research summaries
- Save research output to a file

The system uses:
- LangChain Tool Calling Agent
- Groq LLaMA 3.1 model
- Pydantic structured output parser
- DuckDuckGo and Wikipedia tools
"""
# Import environment variable loader
from dotenv import load_dotenv

# Import BaseModel for structured output
from pydantic import BaseModel

# Import Groq LLM wrapper
from langchain_groq import ChatGroq

# Import prompt template
from langchain_core.prompts import ChatPromptTemplate

# Import parser to convert LLM output into structured format
from langchain_core.output_parsers import PydanticOutputParser

# Import tool-calling agent creator
from langchain.agents.tool_calling_agent import create_tool_calling_agent

# Import agent executor to run the agent
from langchain_core.agents import AgentExecutor

import os

# Load API key from .env file
load_dotenv()


# Define the structure of the research output using Pydantic
class ResearchResponse(BaseModel):
    topic: str        # Research topic name
    summary: str      # Summary of the research
    sources: list[str]   # Sources used (Wikipedia, Web, etc.)
    tools_used: list[str]  # Tools used by the agent


# Initialize the Groq LLaMA model
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),  # Load Groq API key
    model="llama-3.1-8b-instant",       # LLaMA model
    temperature=0                       # Deterministic output
)


# Create a parser that converts LLM output into ResearchResponse format
parser = PydanticOutputParser(pydantic_object=ResearchResponse)


# Create the prompt template for the agent
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use necessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),

        # Chat history placeholder (optional memory)
        ("placeholder", "{chat_history}"),

        # User query input
        ("human", "{query}"),

        # Agent scratchpad (used internally for tool reasoning)
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())


# Create the tool-calling agent
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)


# Create agent executor (runs the agent + tools)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True   # Shows tool usage in terminal
)


# Take research query from user
query = input("What can I help you research? ")


# Run the agent
raw_response = agent_executor.invoke({"query": query})


# Try to parse the structured output
try:
    structured_response = parser.parse(raw_response["output"])
    print(structured_response)

# If parsing fails, print error and raw output
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)