from datetime import datetime
from enum import auto
from typing import List, Optional

from core.dependencies import login_manager

from database.model import Todo, TodoIn, TodoUpdate, User, UserIn, UserUpdate


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


async def read_todo_by_id(id: int) -> Todo:
    return await Todo.get(id=id)


async def read_todo_by_user(todo_id: int, user: User) -> Todo:
    return await Todo.get(id=todo_id, author_id=user)


async def read_all_todo_by_user(user: User) -> List[Todo]:
    return await Todo.filter(author_id=user)


async def update_todo(todo: TodoUpdate) -> Todo:
    todo_db_model = await Todo.get(id=todo.id)
    todo_db_model.update_from_dict(todo.dict(exclude_unset=True, exclude={"id"}))
    await todo_db_model.save()
    return todo_db_model


async def update_todo_by_user(todo: TodoUpdate, user: User) -> Todo:
    todo_db_model = await Todo.get(id=todo.id, author_id=user)
    todo_db_model.update_from_dict(todo.dict(exclude_unset=True, exclude={"id"}))
    await todo_db_model.save()
    return todo_db_model
