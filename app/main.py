from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.ai import router as ai_router
from fastapi.responses import FileResponse

app = FastAPI(
    title="OpenAI APIs",
    version="0.1.0",
    description="FastAPI backend application that provides OpenAI services",
    docs_url="/docs",
    redoc_url=None,
)

app.include_router(ai_router)


app.mount("/", StaticFiles(directory="static", html=True), name="static")

