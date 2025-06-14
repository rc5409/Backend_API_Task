import asyncio
from openai import OpenAI, RateLimitError, APIConnectionError
from fastapi import HTTPException
from app.utils.config import get_settings

settings = get_settings()
client = OpenAI(api_key=settings.openai_api_key)

MAX_RETRIES = 3
DELAY = 2  # seconds

async def ask_openai(prompt: str) -> str:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            chat = client.chat.completions.create(
            model=settings.model,
            messages=[{"role": "user", "content": prompt}],
            timeout=15,
            )           
            return chat.choices[0].message.content.strip()

        except RateLimitError:
            if attempt == MAX_RETRIES:
                raise HTTPException(status_code=429, detail="OpenAI rate limit reached")
            await asyncio.sleep(DELAY * attempt)  # exponential-ish back-off

        except APIConnectionError:
            raise HTTPException(status_code=503, detail="OpenAI connection error")

        except Exception as exc:
            raise HTTPException(status_code=502, detail=f"OpenAI error: {exc}")
