from datetime import datetime
from typing import List

from core.models.model import TodoOut


todo_db: List[TodoOut] = [
    TodoOut(
        id=1,
        title="First Todo",
        content="A todo list content test",
        author="test_user_1",
        created_at=datetime.now(),
    ),
    TodoOut(
        id=2,
        title="Second Todo",
        content="Test content 2",
        author="test_user_1",
        created_at=datetime.now(),
    ),
]
