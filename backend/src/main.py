from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.notifications import router as notification_router
from src.api.task import router as task_router
from src.api.user import router as user_router
from src.broker import broker
from src.config import settings
from src.loggin_config import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    await broker.start()
    yield
    await broker.stop()

setup_logging()

app = FastAPI(title="ToDoApp", lifespan=lifespan)

app.include_router(task_router)
app.include_router(user_router)
app.include_router(notification_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.FRONTEND_URL,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
