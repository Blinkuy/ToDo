from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.task import router as task_router
from src.config import settings

app = FastAPI(title="ToDoApp")

app.include_router(task_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.FRONTEND_URL,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
