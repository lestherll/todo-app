from core.models.model import User, UserOut
from core.dependencies import login_manager


@login_manager.user_loader()
async def get_user_by_id(id: int) -> User:
    return User.get(id=id)


async def get_user_by_username(username: str) -> User:
    return await User.get(username=username)
