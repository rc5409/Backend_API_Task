# Ask-AI – FastAPI + OpenAI GPT Integration

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

---

## Project Structure

```
project-root/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── ai.py
│   ├── services/
│   │   └── openai_service.py
│   ├── utils/
│   │   ├── config.py
│   │   └── errors.py
│   └── storage.py
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/rc5409/Backend_API_Task.git
cd Backend_API_Task
```

### 2. Create and activate a virtual environment
python -m venv AI_api
AI_api\Scripts\activate    # Windows
# OR
source AI_api/bin/activate  # macOS/Linux

### 3. Create .env file
```bash
cp .env.example .env
```

Edit your `.env` file to add your OpenAI API key:

```
OPENAI_API_KEY=sk-REPLACE_ME
MODEL=gpt-3.5-turbo
```


### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the server
```bash
uvicorn app.main:app --reload
```

#### Docs UI
```bash
http://127.0.0.1:8000/docs
```

### 6. Test Endpoints
```bash
curl -X POST http://127.0.0.1:8000/ask-ai/translate ^
  -H "Content-Type: application/json" ^
  -d "{\"text\": \"Hello, how are you?\", \"lang\": \"French\"}"
```

### 7. Get Conversation History
```bash
curl -X GET http://127.0.0.1:8000/ask-ai/conversations
```

### 8. Clear History

```bash
curl -X DELETE http://127.0.0.1:8000/ask-ai/conversations

```










