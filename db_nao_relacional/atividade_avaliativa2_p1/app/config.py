from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings (BaseSettings):
    MONGO_URL: str
    MONGO_DB: str = "chatdb"

    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding='utf-8')

settings = Settings()