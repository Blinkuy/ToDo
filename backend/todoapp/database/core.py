from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from todoapp.database.models import Task
from todoapp.database.database import engine
from todoapp.schemas.task import STaskAdd


class TaskORM:
    
    
    @classmethod
    def create_table(cls) -> None:
        Task.metadata.create_all(bind=engine)
    
    
    @classmethod
    def drop_table(cls) -> None:
        Task.metadata.drop_all(bind=engine)
    
    
    @classmethod
    def get_one_or_none(cls, id: int) -> Task:
        
        with Session(bind=engine) as session:
            stmt = select(Task).where(Task.task_id == id)
            
            result = session.execute(stmt).scalar_one_or_none()
            
        return result
    
    
    @classmethod
    def add_one(cls, task_data: STaskAdd) -> None:
        
        with Session(bind=engine) as session:
            
            task_data = Task(**task_data.model_dump())
            session.add(task_data)
            
            session.commit()
            
            
    @classmethod
    def get_all_by_user_id(cls, user_id: id):
        
        with Session(bind=engine) as session:
            smth = select(Task).where(Task.user_id==user_id)
            
            result = session.execute(smth).scalars().all()
            
        return result
    
    
    @classmethod
    def delete_one(cls, task_id: int):

        with Session(bind=engine) as session:
            
            stmt = delete(Task).where(Task.task_id==task_id)
            
            result = session.execute(stmt)
            
            session.commit()
        
        return result.rowcount
