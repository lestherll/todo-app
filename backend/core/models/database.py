from core.schemas.schema import TodoOut
from typing import List
from datetime import datetime


todo_db: List[TodoOut] = [
    TodoOut(
        title="First Todo",
        content="A todo list content test",
        author="test_user_1",
        date_created=datetime.now(),
    ),
    TodoOut(
        title="Second Todo",
        content="Test content 2",
        author="test_user_1",
        date_created=datetime.now(),
    ),
]
