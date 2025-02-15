from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from src.exception import CustomException
from src.logger import get_logger

logger = get_logger(__name__)

class ModelLoader:
    """Loads different AI models for processing queries."""
    
    def __init__(self):
        try:
            self.google_llm = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
            self.groq_llm = ChatGroq(model="llama-3.3-70b-versatile")
            logger.info("Models initialized successfully.")
        except Exception as e:
            raise CustomException("Error initializing models", e)
    
    def get_model(self, provider: str, model_name: str):
        """Returns a model based on provider and model name."""
        try:
            if provider == "Groq":
                return ChatGroq(model=model_name)
            elif provider == "GoogleGenerativeAI":
                return ChatGoogleGenerativeAI(model=model_name)
            else:
                raise ValueError("Invalid provider")
        except Exception as e:
            raise CustomException(f"Error loading model: {model_name}", e)
