import os
import sys


from src.logger import get_logger
from src.exception import CustomException

from dotenv import load_dotenv
from src.exception import CustomException
from src.logger import get_logger

logger = get_logger(__name__)



from src.logger import logging
from src.exception import CustomException

class DataIngestion:
    """Handles API key loading and environment setup."""
    
    def __init__(self):
        try:
            load_dotenv()
            self.tavily_api_key = os.getenv("TAVILY_API_KEY")
            self.langsmith_api_key = os.getenv("LANGSMITH_API_KEY")
            self.google_api_key = os.getenv("GOOGLE_API_KEY")
            self.groq_api_key = os.getenv("GROQ_API_KEY")
            logger.info("API keys loaded successfully.")
        except Exception as e:
            raise CustomException("Error loading API keys", e)
    
    def get_api_keys(self):
        """Returns API keys."""
        return {
            "TAVILY_API_KEY": self.tavily_api_key,
            "LANGSMITH_API_KEY": self.langsmith_api_key,
            "GOOGLE_API_KEY": self.google_api_key,
            "GROQ_API_KEY": self.groq_api_key,
        }
