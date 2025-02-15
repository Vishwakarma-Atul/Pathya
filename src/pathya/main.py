from fastapi import FastAPI
from .api import chat

app = FastAPI(title="Pathya Chatbot")

app.include_router(chat.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port='5055')

## uvicorn main:app --host 0.0.0.0 --port 5055 --reload
