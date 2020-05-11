from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from ..services import util, messages

router = APIRouter()

@router.get("/")
def get():
    return messages.all() 

class Message(BaseModel):
    text: str

@router.post("/add")
def add(message: Message, authorization: str = Header(None)):
    user_id = util.token_to_userid(authorization)
    if not user_id:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    response = messages.add(user_id, message.text)
    return {"msg": response}
