from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.lm_studio import call_lm_studio
from .utils import logging

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

# just very basic api to /chat
@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(chat: ChatRequest):
    # shall be logged
    if not chat.message:
        logging.log_error("message cannot be empty.")
        raise HTTPException(status_code=400, detail="Message cannot be empty.")
    
    reply = call_lm_studio(chat.message)
    logging.log_info(f"reply: {reply}")
    return ChatResponse(reply=reply)
