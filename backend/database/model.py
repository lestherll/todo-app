from tortoise import fields, models
from tortoise.contrib.pydantic.creator import pydantic_model_creator


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=30)
    email = fields.CharField(max_length=50)
    password = fields.CharField(max_length=256)
    created_at = fields.DatetimeField(auto_now_add=True)

    class PydanticMeta:
        ...


UserIn = pydantic_model_creator(User, name="UserIn", exclude=("id", "created_at"))
UserOut = pydantic_model_creator(
    User, name="UserOut", exclude=("created_at", "password")
)
UserUpdate = pydantic_model_creator(
    User, name="UserUpdate", exclude=("id", "created_at")
)


class Todo(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=50)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    author_id: fields.ForeignKeyRelation[User] = fields.ForeignKeyField("models.User")

    class PydanticMeta:
        ...


TodoIn = pydantic_model_creator(Todo, name="TodoIn", exclude=("id", "created_at"))
TodoOut = pydantic_model_creator(Todo, name="TodoOut")
TodoUpdate = pydantic_model_creator(Todo, name="TodoUpdate", exclude=("created_at",))
