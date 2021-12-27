from fastapi_login import LoginManager
from core.config import settings


login_manager = LoginManager(
    secret=settings.SECRET_KEY,
    token_url=settings.TOKEN_URL,
)
