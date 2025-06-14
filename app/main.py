from fastapi import FastAPI
from app.routes.ai import router as ai_router

app = FastAPI(
    title="OpenAI APIs",
    version="0.1.0",
    description="FastAPI backend Application integrated with OpenAI API",
    docs_url="/docs",
    redoc_url=None,
)

app.include_router(ai_router)

### test ###
# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
