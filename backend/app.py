from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.lm_studio import call_lm_studio
from utils import logging

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

class ChatReply(BaseModel):
    reasoning: str
    reply: str

class ChatResponse(BaseModel):
    reply: ChatReply

# just very basic api to /chat
@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(chat: ChatRequest):
    # shall be logged
    if not chat.message:
        logging.log_error("message cannot be empty.")
        raise HTTPException(status_code=400, detail="Message cannot be empty.")
    
    reply = call_lm_studio(chat.message)
    # we need to ensure 'reply' is a valid dictionary [object Object] error in js...
    if isinstance(reply, dict) and 'reasoning' in reply and 'reply' in reply:
        chat_reply = ChatReply(reasoning=reply['reasoning'], reply=reply['reply'])
    else:
        logging.log_error("Invalid reply structure from LM Studio")
        raise HTTPException(status_code=500, detail="Error with the LM Studio response")
    
    logging.log_info(f"reply: {chat_reply}")
    return ChatResponse(reply=chat_reply)
