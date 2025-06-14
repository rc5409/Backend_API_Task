from fastapi import APIRouter, HTTPException
from app.utils.schemas import AskRequest, AskResponse
from app.controllers.ai_controller import handle_prompt
from app.storage import get_all, clear_all

router = APIRouter(tags=["ai"])

@router.post("/ask-ai", response_model=AskResponse)
async def ask_ai(body: AskRequest):
    if not body.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt must not be empty")
    return await handle_prompt(body.prompt)

@router.get("/conversations")
async def list_conversations():
    return get_all()

@router.delete("/conversations")
async def delete_conversations():
    clear_all()
    return {"detail": "History cleared"}
