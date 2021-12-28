from typing import List

from core.dependencies import login_manager
from database import crud
from database.model import Todo, TodoIn, TodoOut, TodoUpdate, User
from fastapi import APIRouter
from fastapi.param_functions import Depends

router = APIRouter(
    prefix="/todos", tags=["todos"], responses={404: {"description": "Not found"}}
)


@router.get("/", response_model=List[TodoOut])
async def read_todos():
    return await TodoOut.from_queryset(Todo.all())


@router.post("/", response_model=TodoOut)
async def create_todo(todo: TodoIn, author: User = Depends(login_manager)):
    new_todo = await crud.create_todo(todo, author)
    return await TodoOut.from_tortoise_orm(new_todo)


@router.put("/", response_model=TodoOut)
async def update_todo(todo: TodoUpdate):
    await Todo.filter(id=todo.id).update(
        **todo.dict(exclude_unset=True, exclude={"id"})
    )
    return await TodoOut.from_queryset_single(Todo.get(id=todo.id))


@router.delete("/", response_model=TodoOut)
async def delete_todo(todo_id: int):
    todo_to_delete = await Todo.filter(id=todo_id).get()
    await todo_to_delete.delete()
    return todo_to_delete
