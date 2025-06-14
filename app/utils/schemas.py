from pydantic import BaseModel, Field

class AskRequest(BaseModel):
    prompt: str = Field(..., example="Ask me Anything!")

class AskResponse(BaseModel):
    id: str
    timestamp: str
    prompt: str
    answer: str
