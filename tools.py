# Import tools from LangChain community
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun, ArxivQueryRun

# Import API wrappers for Wikipedia and Arxiv
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper

# Import Tool class to create custom tools
from langchain.tools import Tool

# Import datetime to add timestamp and current date
from datetime import datetime


# Function to save research output to a text file
def save_to_txt(data: str, filename: str = "research_output.txt"):
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Format the text to be saved
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    # Open file in append mode and save the data
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    # Return success message
    return f"Data successfully saved to {filename}"


# Function to get current date (useful for research reports)
def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")


# Tool 1: Save research report to text file
save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Use this tool to save the final research report to a text file."
)


# Tool 2: DuckDuckGo search tool (for web search)
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Use this tool to search the internet for current information and recent events."
)


# Tool 3: Wikipedia search tool (for general knowledge)
api_wrapper = WikipediaAPIWrapper(
    top_k_results=2,              # Number of results to fetch
    doc_content_chars_max=1000    # Max characters per result
)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)


# Tool 4: Arxiv research paper search tool (for academic papers)
arxiv = ArxivQueryRun(
    api_wrapper=ArxivAPIWrapper(top_k_results=2)
)


# Tool 5: Current date tool (useful for adding date in research report)
date_tool = Tool(
    name="current_date",
    func=get_current_date,
    description="Returns the current date."
)


# List of all tools used by the AI research agent
tools = [search_tool, wiki_tool, arxiv, save_tool, date_tool]