'''
Phase 2: Setup Backend with the FastAPI

Step 1: Setup Pydantic Model (Schema Validation)
Step 2: Setup AI Agent From FrontEnd Request
Step 3: Run app and Explore Swagger UI Docs
'''

# Step 1: Setup Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List
from old.ai_agent import get_response_from_ai_agent

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

# Step 2: Setup AI Agent From FrontEnd Request
from fastapi import FastAPI

ALLOWED_MODEL_NAMES = [ 
    "llama-3.3-70b-versatile",
    "mixtral-8x7b-32768", 
    "llama3-70b-8192"
]

app = FastAPI(title = "Langgrah AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    It is a API Endpoint to interact with the Chatbot using the
    LangGraph and Search Tools. 
    It selected the model specified in the request.
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid modle name"}
    
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    # Create AI Agent and get the response  from it
    response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return response


# Step 3: Run app and Explore Swagger UI Docs using UVICORN
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port = 9999)