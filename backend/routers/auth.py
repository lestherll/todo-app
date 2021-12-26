from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from core.models import crud
from core.dependencies import login_manager


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login")
async def login(data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password

    user = await crud.get_user_by_username(username)
    if not user:
        raise InvalidCredentialsException
    elif password != user.password:
        raise InvalidCredentialsException

    access_token = login_manager.create_access_token(data={"sub": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
