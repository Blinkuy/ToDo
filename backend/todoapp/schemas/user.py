from pydantic import BaseModel


class SUserAdd(BaseModel):
    username: str
    password: str


class SUser(SUserAdd):
    user_id: int
