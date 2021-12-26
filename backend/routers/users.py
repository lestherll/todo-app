from typing import List
from fastapi import APIRouter, Depends
from core.models.model import User, UserIn, UserOut, UserUpdate
from core.dependencies import login_manager
from datetime import datetime

router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not found"}}
)


@router.get("/", response_model=List[UserOut])
async def read_users():
    return await UserOut.from_queryset(User.all())


@router.post("/", response_model=UserOut)
async def create_user(user: UserIn):
    user_obj = await User.create(
        **user.dict(exclude_unset=True), created_at=datetime.now()
    )
    return await UserOut.from_tortoise_orm(user_obj)


@router.put("/", response_model=UserOut)
async def update_user(user: UserUpdate):
    await User.filter(id=user.id).update(
        **user.dict(exclude_unset=True, exclude={"id"})
    )
    return await UserOut.from_queryset_single(User.get(id=user.id))


@router.get("/me", response_model=UserOut)
async def read_current_user(user=Depends(login_manager)):
    return await UserOut.from_queryset_single(user)
