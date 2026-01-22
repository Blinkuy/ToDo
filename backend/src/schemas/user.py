from src.database.models import User
from src.schemas.base import BaseSchema


class UserCreateRequest(BaseSchema):
    username: str
    password: str


class UserResponse(BaseSchema[User]):
    id: int
    username: str
