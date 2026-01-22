from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.task import router as task_router
from src.api.user import router as user_router
from src.api.notifications import router as notification_router
from src.config import settings
from src.fs_broker import broker


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Broker up")
    await broker.start()
    yield
    print("Broker down")
    await broker.stop()


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
