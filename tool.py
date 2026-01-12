from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool # Modern import path
from datetime import datetime

# ---------------- Save to File Tool ---------------- #
@tool
def save_tool(data: str):
    """Saves research data to a text file named research_output.txt."""
    filename = "research_output.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    return f"Successfully saved to {filename}"

# ---------------- DuckDuckGo Search Tool ---------------- #
@tool
def search_tool(query: str):
    """Search the web for current events and real-time info."""
    search = DuckDuckGoSearchRun()
    return search.run(query)

# ---------------- Wikipedia Tool ---------------- #
@tool
def wiki_tool(query: str):
    """Query Wikipedia for historical facts and general summaries."""
    # We define the wrapper inside to ensure it validates the environment correctly
    api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=800)
    wiki = WikipediaQueryRun(api_wrapper=api_wrapper)
    return wiki.run(query)