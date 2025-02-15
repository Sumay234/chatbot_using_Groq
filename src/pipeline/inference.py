from langgraph.prebuilt import create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages.ai import AIMessage
from src.components.model_loading import ModelLoader
from src.exception import CustomException
from src.logger import get_logger

logger = get_logger(__name__)

class AIAgent:
    """Manages AI agent interactions."""
    
    def __init__(self):
        self.model_loader = ModelLoader()
    
    def get_response(self, llm_id, query, allow_search, system_prompt, provider):
        """Gets response from AI agent."""
        try:
            llm = self.model_loader.get_model(provider, llm_id)
            tools = [TavilySearchResults(max_results=2)] if allow_search else []
            
            agent = create_react_agent(
                model=llm,
                tools=tools,
                state_modifier=system_prompt
            )
            
            state = {"messages": [("user", query)]}
            response = agent.invoke(state)
            messages = response.get("messages", [])
            
            ai_message = [msg.content for msg in messages if isinstance(msg, AIMessage)]
            return ai_message[-1] if ai_message else "No response received."
        except Exception as e:
            raise CustomException("Error in AI Agent response generation", e)
