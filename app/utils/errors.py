from fastapi import HTTPException

def raise_invalid_input(message="Invalid input"):
    raise HTTPException(status_code=400, detail=message)

def raise_openai_rate_limit():
    raise HTTPException(status_code=429, detail="OpenAI rate limit reached")

def raise_openai_failure(error):
    raise HTTPException(status_code=502, detail=f"OpenAI error: {error}")

def raise_openai_unavailable():
    raise HTTPException(
        status_code=503,
        detail="Upstream OpenAI service is unavailable. Please retry after a few seconds."
    )
