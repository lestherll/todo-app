from datetime import datetime

from core.dependencies import login_manager

from database.model import Todo, TodoIn, User, UserIn, UserUpdate


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


async def create_todo(todo: TodoIn, author: User) -> Todo:
    return await Todo.create(
        **todo.dict(exclude_unset=True), author_id=author, created_at=datetime.now()
    )
