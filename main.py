import os
import sys
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

# Fix for ModuleNotFoundError
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from tool import save_tool, search_tool, wiki_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str = Field(description="The main subject of research")
    summary: str = Field(description="A detailed summary of findings")
    sources: list[str] = Field(description="List of sources used")

# 1. Setup LLM
llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0)
tools = [save_tool, search_tool, wiki_tool]
llm_with_tools = llm.bind_tools(tools)

def run_app():
    query = input("What do you want to research? ")
    
    # Create a conversation history
    messages = [HumanMessage(content=f"Research the following topic, save the results to a file, and then provide a summary: {query}")]
    
    # 2. First Pass: AI decides to use Search/Wiki and Save tools
    ai_msg = llm_with_tools.invoke(messages)
    messages.append(ai_msg)
    
    if ai_msg.tool_calls:
        for tool_call in ai_msg.tool_calls:
            # Match the tool name to our actual functions
            selected_tool = {
                "save_tool": save_tool, 
                "search_tool": search_tool, 
                "wiki_tool": wiki_tool
            }[tool_call["name"]]
            
            print(f"Executing: {tool_call['name']}...")
            tool_output = selected_tool.invoke(tool_call["args"])
            
            # Feed the tool result back into the message history
            messages.append(ToolMessage(content=str(tool_output), tool_call_id=tool_call["id"]))
    
    # 3. Second Pass: Get Structured Output based on the findings now in 'messages'
    print("Synthesizing final report...")
    structured_llm = llm.with_structured_output(ResearchResponse)
    
    # We pass the whole conversation history so the LLM "remembers" the tool results
    final_report = structured_llm.invoke(messages)
    
    print("\n--- FINAL REPORT ---")
    print(f"TOPIC: {final_report.topic}")
    print(f"SUMMARY: {final_report.summary}")
    print(f"SOURCES: {final_report.sources}")
    print("\nCheck 'research_output.txt' for the saved data!")

if __name__ == "__main__":
    run_app()