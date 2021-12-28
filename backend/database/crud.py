from datetime import datetime
from database.model import User, UserIn, UserOut, UserUpdate
from core.dependencies import login_manager


@login_manager.user_loader()
async def get_user_by_id(id: int) -> User:
    return await User.get(id=id)


async def get_user_by_username(username: str) -> User:
    return await User.get(username=username)


async def create_user(user: UserIn) -> User:
    return await User.create(**user.dict(exclude_unset=True), created_at=datetime.now())


async def update_user(user: User, new_user_details: UserUpdate) -> User:
    await user.update_from_dict(new_user_details.dict(exclude_unset=True))
    await user.save()
    return user
