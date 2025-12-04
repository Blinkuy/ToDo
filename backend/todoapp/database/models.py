from sqlalchemy import DateTime, func

from sqlalchemy.orm import (
    DeclarativeBase,
    MappedAsDataclass,
    Mapped, mapped_column,
)

import datetime 


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "task"

    task_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    
    name: Mapped[str]
    description: Mapped[str]

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    
    def __repr__(self):
        return f"Task object: (id:{self.task_id}, name:{self.name})"


class User(Base):
    __tablename__ = "user"
    
    user_id: Mapped[int] = mapped_column(primary_key=True)
    
    username: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    

Base.metadata.create_all()