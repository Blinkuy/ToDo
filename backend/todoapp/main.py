from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

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
