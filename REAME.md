# 🤖 Python AI Research Agent

An intelligent research assistant powered by **Gemini 2.0 Flash** and **LangChain**. This agent can search the web, query Wikipedia, and automatically save a structured research report to a local file.

## 🚀 Features
* **Web Search:** Real-time info via DuckDuckGo.
* **Knowledge Base:** Historical facts from Wikipedia.
* **Auto-Save:** Automatically logs findings to `research_output.txt`.
* **Structured Output:** Delivers findings in a clean Pydantic-validated format.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Hamama-Komal/Python_AI_Model.git](https://github.com/Hamama-Komal/Python_AI_Model.git)
   cd Python_AI_Model

2. **Set Up a Virtual Environment:**

# Create the environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate

3. **Install Dependencies:**

pip install langchain-google-genai langchain-community wikipedia duckduckgo-search pydantic python-dotenv

5. **Configure Environment Variables:**

Create a file named .env in the root folder and add your Google Gemini API Key:
GOOGLE_API_KEY=your_actual_key_here


6. **💻 Usage:**

Run the main script and enter your topic when prompted. The agent will decide which tools to use, execute the research, and save the result.
python main.py


## 📂 Project Structure

* main.py: The core application logic and AI message orchestration.
* tool.py: Custom definitions for the Search, Wikipedia, and File-Saving tools.
* research_output.txt: (Auto-generated) The local log of all research findings.
* .env: (Ignored) Contains your private API keys.
* .gitignore: Prevents sensitive files and virtual environments from being pushed to GitHub.

# Developed with ❤️ using Gemini & LangChain
