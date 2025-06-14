# AI_api – Prompt-to-AI Backend (FastAPI)

This is a simple backend API that securely connects to an AI model (e.g., OpenAI GPT) to process user prompts and return generated responses. It is built with FastAPI and follows best practices for modular design, environment-based API key management, and optional conversation logging.

---

##  Features

- `POST /ask-ai` — Send a user prompt and receive an AI-generated response
- `GET /conversations` — Retrieve previous prompt-response pairs (in-memory)
- `DELETE /conversations` — Clear conversation history
- OpenAPI docs at `/docs` (Swagger UI)
- Environment variable-based secret loading (`.env` file)
- Modular folder structure: `routes/`, `controllers/`, `services/`, `utils/`

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/AI_api.git
cd AI_api
```

### 2. Create and activate a virtual environment
python -m venv AI_api
AI_api\Scripts\activate    # Windows
# OR
source AI_api/bin/activate  # macOS/Linux

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the server
uvicorn main:app --reload

#### Docs UI
http://127.0.0.1:8000/docs


### 5. Test Endpoints
curl -X POST http://127.0.0.1:8000/ask-ai \
  -H "Content-Type: application/json" \
  -d "{\"prompt\": \"Translate hello to Spanish\"}"

#### sample response
{
  "id": "ab1234...",
  "timestamp": "2025-06-13T20:45:02.123Z",
  "prompt": "Translate hello to Spanish",
  "answer": "Hola"
}

#### Clear History
curl -X DELETE http://127.0.0.1:8000/conversations

## Project Structure
AI_api/
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── ai.py
│   ├── controllers/
│   │   └── ai_controller.py
│   ├── services/
│   │   └── openai_service.py
│   ├── utils/
│   │   ├── config.py
│   │   └── schemas.py
│   └── storage.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md




