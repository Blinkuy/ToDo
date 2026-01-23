from typing import Generic, Type, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound="BaseSchema")
M = TypeVar("M")

class BaseSchema(BaseModel, Generic[M]):
    model_config = {
        "from_attributes": True,
    }

    @classmethod
    def from_orm_to_model(cls: Type[T], obj: M):
        return cls.model_validate(obj)
