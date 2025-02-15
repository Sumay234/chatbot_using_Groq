'''
Phase 1 - Creating the AI Agent

# Step 1 : SetUp API KEY for Groq and Tavily
# Step 2 : SetUp LLM & Tools
# Step 3 : Setup AI Agent with Search tool Functionality

'''

# Step 1 : SetUp API KEY for Groq and Tavily

import os
from dotenv import load_dotenv
load_dotenv()


TAVILY_API_KEY = os.getenv("TAVILY_API_KEY") 
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Step 2 : SetUp LLM & Tools
from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAI , ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults

from langchain_core.messages.ai import AIMessage

# LLM model setup
google_llm = ChatGoogleGenerativeAI(model = "gemini-pro",convert_system_message_to_human=True )
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")

# Tools setup
search_tool = TavilySearchResults(max_results=5)

#Step 3 : Setup AI Agent with Search tool Functionality
from langgraph.prebuilt import create_react_agent

system_prompt = "Act as an AI ChatBot who is Smart , Intelligent and Friendly"


def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "GoogleGenerativeAI":
        llm = ChatGoogleGenerativeAI(model = llm_id)
    
    
    tools = [TavilySearchResults(max_results=2)]  if allow_search else [] # Tools setup
    agent = create_react_agent(
        model=  llm,
        tools = tools,
        state_modifier = system_prompt
    )


   # query = ""
    # state = {"message" : query}
    state = {"messages": [("user", query)]}
    respone = agent.invoke(state)
    messages = respone.get("messages")
    ai_message = [message.content for message in messages if isinstance(message, AIMessage)]
    return (ai_message[-1]) 
'''    ai_message = []
    for messages in messages:
        if isinstance(messages, AIMessage):
            ai_message.append(messages.content)
'''         