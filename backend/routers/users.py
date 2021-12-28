from typing import List
from database import crud

from core.dependencies import login_manager
from database.model import User, UserOut, UserUpdate
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[UserOut])
async def read_users():
    return await UserOut.from_queryset(User.all())


@router.put("/", response_model=UserOut)
async def update_user(user: UserUpdate, current_user: User = Depends(login_manager)):
    current_user = await crud.update_user(current_user, user)
    return await UserOut.from_tortoise_orm(current_user)


@router.get("/me", response_model=UserOut)
async def read_current_user(user: User = Depends(login_manager)):
    return await UserOut.from_tortoise_orm(user)
