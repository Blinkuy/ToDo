from fastapi import APIRouter

from todoapp.database.core import TaskORM
from todoapp.schemas.task import STask, STaskAdd

router = APIRouter(prefix="/task", tags=["Task"])


@router.get("/get_all", response_model=list[STask])
def get_tasks(user_id: int): #add limit 
    result = TaskORM.get_all_by_user_id(user_id=user_id)
    
    return result


@router.post("/add")
def add_task(task: STaskAdd):
    
    TaskORM.add_one(task_data=task)


@router.delete("/delete")
def delete_task(task_id: int):
    res = TaskORM.delete_one(task_id)
    
    if res == 0:
        return {"detail": "Task not found"}
    return {"detail": "Task deleted successfully"}

