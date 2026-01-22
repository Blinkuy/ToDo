import datetime

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    username: Mapped[str] = mapped_column(
        String(256),
        unique=True,
        nullable=False,
    )

    password: Mapped[str] = mapped_column(
        String(256),
        nullable=False,
    )

    tasks: Mapped[list["Task"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    notifications: Mapped[list["Notification"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )


class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(256),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String(1024),
        nullable=True,
    )

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    user: Mapped["User"] = relationship(
        back_populates="tasks",
    )

    notifications: Mapped[list["Notification"]] = relationship(
        back_populates="task",
        cascade="all, delete-orphan",
    )


class Notification(Base):
    __tablename__ = "notification"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
    )

    task_id: Mapped[int] = mapped_column(
        ForeignKey("task.id", ondelete="CASCADE"),
        nullable=False,
    )

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    user: Mapped["User"] = relationship(back_populates="notifications")

    task: Mapped["Task"] = relationship(back_populates="notifications")
