from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    GEMINI_API_KEY: Optional[str] = "AIzaSyDIxxYQMnpwQdNkpwdZBkC4gCDEThrCjsc"
    Client_ID: Optional[str] = "lSXz7ICBL_DP1Sz7SG46nQ"
    Client_Secret: Optional[str] = "AqBoIUoam2OknEKW9Qu0Mz2eD5Uv6g"
    User_Agent: Optional[str] = "redit-persona"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()