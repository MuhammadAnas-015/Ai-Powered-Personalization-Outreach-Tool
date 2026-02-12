import os
from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv

# Load .env file explicitly for local development
load_dotenv()

class Settings(BaseSettings):
    # Try GEMINI_API_KEY first (as requested), then GOOGLE_API_KEY, then fallback
    google_api_key: str = os.getenv("GEMINI_API_KEY", os.getenv("GOOGLE_API_KEY", ""))
    
    huggingface_api_token: str = os.getenv("HUGGINGFACE_API_TOKEN", "")
    app_title: str = "AI-Powered Outreach Tool"
    app_description: str = "Generate personalized B2B cold emails using AI"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

@lru_cache()
def get_settings():
    return Settings()
