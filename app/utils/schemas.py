from pydantic import BaseModel, Field

class AskRequest(BaseModel):
    prompt: str = Field(..., example="Translate hello to Spanish")

class AskResponse(BaseModel):
    id: str
    timestamp: str
    prompt: str
    answer: str
