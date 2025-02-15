from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from src.pipeline.inference import AIAgent
from src.exception import CustomException
from src.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(title="LangGraph AI Agent")
ai_agent = AIAgent()

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

ALLOWED_MODEL_NAMES = [
    "llama-3.3-70b-versatile",
    "mixtral-8x7b-32768",
    "llama3-70b-8192",
    "gemini-pro"
]

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """Handles chat queries."""
    try:
        if request.model_name not in ALLOWED_MODEL_NAMES:
            return {"error": "Invalid model name"}
        
        response = ai_agent.get_response(
            llm_id=request.model_name,
            query=request.messages[0],
            allow_search=request.allow_search,
            system_prompt=request.system_prompt,
            provider=request.model_provider
        )
        return {"response": response}
    except Exception as e:
        raise CustomException("Error processing chat request", e)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)
