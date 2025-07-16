from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GEMINI_API_KEY: str = None
    Client_ID: str = None
    Client_Secret: str = None
    User_Agent: str = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()