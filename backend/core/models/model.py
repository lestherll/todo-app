from tortoise import fields, models
from tortoise.contrib.pydantic.creator import pydantic_model_creator


class Todo(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=50)
    content = fields.TextField()
    author = fields.CharField(max_length=50)
    created_at = fields.DatetimeField(auto_now_add=True)

    class PydanticMeta:
        ...


TodoIn = pydantic_model_creator(
    Todo, name="TodoIn", exclude=("id", "created_at", "author")
)
TodoOut = pydantic_model_creator(Todo, name="TodoOut")
TodoUpdate = pydantic_model_creator(
    Todo, name="TodoUpdate", exclude=("created_at", "author")
)
