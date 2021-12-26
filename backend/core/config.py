from pydantic import BaseSettings


class _Settings(BaseSettings):
    SECRET_KEY: str
    DB_URI: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = _Settings()
