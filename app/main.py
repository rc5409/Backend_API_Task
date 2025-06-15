# from fastapi import FastAPI
# from app.routes.ai import router as ai_router

# app = FastAPI(
#     title="OpenAI APIs",
#     version="0.1.0",
#     description="FastAPI backend Application integrated with OpenAI API",
#     docs_url="/docs",
#     redoc_url=None,
# )

# app.include_router(ai_router)


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

# Serve the static folder
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Optional: serve index.html directly at root
# @app.get("/")
# async def root():
#     return FileResponse("static/index.html")
# app.include_router(ai_router)

### test ###
# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
