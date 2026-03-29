AI Research Agent using LangChain + Groq (LLaMA 3.1)
📌 Project Description

This project is an AI-powered Research Agent built using LangChain, Groq API, and LLaMA 3.1 model. The agent can search the web, retrieve information from Wikipedia, generate structured research summaries, and save the research output to a text file.

The system uses tool-calling agents, structured output parsing using Pydantic, and multiple research tools to automate the research process.

🚀 Features
AI Research Assistant
Web Search (DuckDuckGo)
Wikipedia Search
Structured Output (Topic, Summary, Sources, Tools Used)
Saves Research Output to Text File
Uses Groq LLaMA 3.1 model for fast inference
Built with LangChain Tool Calling Agent
Uses Pydantic for structured response parsing
🛠️ Technologies Used
Python
LangChain
Groq API (LLaMA 3.1)
Pydantic
DuckDuckGo Search
Wikipedia API
dotenv
📂 Project Structure
project/
│── main.py
│── tools.py
│── .env
│── research_output.txt
│── requirements.txt
⚙️ Setup Instructions
1. Create Virtual Environment
python -m venv research_env
research_env\Scripts\activate
2. Install Dependencies
pip install langchain langchain-core langchain-community langchain-groq python-dotenv pydantic duckduckgo-search wikipedia
3. Add API Key in .env
GROQ_API_KEY=your_api_key_here
4. Run the Project
python main.py
📊 Example Output
Topic: Artificial Intelligence in Healthcare
Summary: AI is used in healthcare for diagnosis, prediction, medical imaging, and automation...
Sources: Wikipedia, DuckDuckGo
Tools Used: search, wikipedia
🎯 Use Cases
Research Paper Writing
Literature Review
Academic Research
Report Generation
Automated Knowledge Gathering
📜 License

This project is for educational and research purposes.
