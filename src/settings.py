from pydantic_settings import BaseSettings
from dotenv import load_dotenv 
import os

mode = os.getenv("MODE", "local")


class Settings(BaseSettings):
    APP_ENV: str = mode
    APP_VERSION: str = "0.0.0"
    DOCS: bool = True


settings = Settings()