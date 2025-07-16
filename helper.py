from crewai import LLM
from config import settings

api_key = settings.GEMINI_API_KEY

def get_llm():
    """Get the LLM object."""
    return LLM(model="gemini/gemini-2.0-flash", api_key=api_key)
