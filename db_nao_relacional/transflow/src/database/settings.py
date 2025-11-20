from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URL: str
    REDIS_HOST: str
    REDIS_PORT: int
    RABBITMQ_URL: str

    class Config:
        env_file = ".env"

settings = Settings()