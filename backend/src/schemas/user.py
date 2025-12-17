from .base import BaseSchema


class UserCreateRequest(BaseSchema):
    username: str
    password: str


class UserResponse(BaseSchema):
    id: int
    username: str
