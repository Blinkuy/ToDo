from polyfactory.factories.sqlalchemy_factory import SQLAlchemyFactory

from src.database.models import Task


class TaskFactory(SQLAlchemyFactory[Task]):
    __model__ = Task
    __set_foreign_keys__ = False
