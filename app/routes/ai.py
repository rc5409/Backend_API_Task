from fastapi import APIRouter
from pydantic import BaseModel
from app.services.openai_service import ask_openai
from app.storage import log_conversation, get_conversations, clear_conversations
from app.utils.errors import raise_invalid_input

router = APIRouter(prefix="/ask-ai", tags=["AI Endpoints"])

class QuestionInput(BaseModel):
    question: str

@router.post("/ask_any_question")
def ask_any_question(data: QuestionInput):
    if not data.question.strip():
        raise_invalid_input("Question cannot be empty.")
    prompt = f"Answer the following question: {data.question}"
    response = ask_openai(prompt)
    log_conversation(prompt, response)
    return {"task": "question", "input": data.question, "output": response}

class TranslateInput(BaseModel):
    text: str
    lang: str = "Spanish"

@router.post("/translate")
def translate(data: TranslateInput):
    if not data.text.strip():
        raise_invalid_input("Text to translate cannot be empty.")
    prompt = f'Translate the following text to {data.lang}: "{data.text}"'
    response = ask_openai(prompt)
    log_conversation(prompt, response)
    return {"task": "translation", "input": data.text, "output": response}

class SummarizeInput(BaseModel):
    text: str

@router.post("/summarize")
def summarize(data: SummarizeInput):
    if not data.text.strip():
        raise_invalid_input("Text to summarize cannot be empty.")
    prompt = f"Summarize the following text: {data.text}"
    response = ask_openai(prompt)
    log_conversation(prompt, response)
    return {"task": "summarization", "input": data.text, "output": response}

@router.get("/conversations")
def show_conversations():
    return get_conversations()

@router.delete("/conversations")
def delete_conversations():
    clear_conversations()
    return {"detail": "Conversation history cleared."}

