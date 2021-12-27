from pydantic import BaseSettings


class _Settings(BaseSettings):
    SECRET_KEY: str
    DB_URI: str
    TOKEN_URL: str = "/auth/login"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = _Settings()
