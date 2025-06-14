from openai import OpenAI, RateLimitError, APIConnectionError
from app.utils.config import get_settings
from app.utils.errors import raise_openai_rate_limit, raise_openai_failure, raise_openai_unavailable
import time

settings = get_settings()
client = OpenAI(api_key=settings.openai_api_key)

def ask_openai(prompt: str) -> str:
    for attempt in range(3):
        try:
            chat = client.chat.completions.create(
                model=settings.model,
                messages=[{"role": "user", "content": prompt}],
                timeout=15,
            )
            return chat.choices[0].message.content.strip()
        except RateLimitError:
            raise_openai_rate_limit()
        except APIConnectionError:
            if attempt == 2:
                raise_openai_unavailable()
            time.sleep(2 * (attempt + 1))
        except Exception as e:
            raise_openai_failure(str(e))