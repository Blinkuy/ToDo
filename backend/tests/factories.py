from polyfactory.factories.sqlalchemy_factory import SQLAlchemyFactory

from src.database.models import Task, User


class TaskFactory(SQLAlchemyFactory[Task]):
    __model__ = Task
    __set_foreign_keys__ = False


class UserFactory(SQLAlchemyFactory[User]):
    __model__ = User
