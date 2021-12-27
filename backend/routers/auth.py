from datetime import datetime

from core.dependencies import login_manager
from database import crud
from database.model import User, UserIn, UserOut
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException

router = APIRouter(prefix="/auth", tags=["auth"])


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


@router.post("/register", response_model=UserOut)
async def create_user(user: UserIn):
    user_obj = await User.create(
        **user.dict(exclude_unset=True), created_at=datetime.now()
    )
    return await UserOut.from_tortoise_orm(user_obj)
