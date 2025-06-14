from fastapi import FastAPI
from app.routes.ai import router as ai_router

app = FastAPI(
    title="AI Backend Assessment",
    description="Prompt in, OpenAI answer out",
    version="1.0.0",
)

app.include_router(ai_router)


# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
