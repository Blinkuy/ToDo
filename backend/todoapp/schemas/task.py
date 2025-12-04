from pydantic import BaseModel

import datetime

class STaskAdd(BaseModel):
    user_id: int
    
    name: str
    description: str
    

class STask(STaskAdd):
    task_id: int
    created_at: datetime.datetime