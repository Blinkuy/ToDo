from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.openapi.docs import get_swagger_ui_html

import dotenv
from os import getenv

from todoapp.database.core import TaskORM
from todoapp.database.models import Task

from todoapp.api.task import router as task_router

app = FastAPI(title="ToDoApp")

app.include_router(task_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:3000",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def redirect_to_docs():
    return RedirectResponse("/docs", status_code=302)
