from uuid import uuid4
from datetime import datetime, timezone
from app.services.openai_service import ask_openai
from app.storage import log_conv

async def handle_prompt(prompt: str) -> dict:
    answer = await ask_openai(prompt)
    record = {
        "id": str(uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "prompt": prompt,
        "answer": answer,
    }
    log_conv(record)
    return record
