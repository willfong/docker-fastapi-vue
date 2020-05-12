from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from ..services import util, users, messages

router = APIRouter()

@router.get("/")
def get():
    return messages.all() 

class Message(BaseModel):
    text: str

@router.post("/add")
def add(message: Message, authorization: str = Header(None)):
    user_detail = users.get_user_data_from_token(authorization)
    if not user_detail:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    response = messages.add(user_detail.get('id'), message.text)
    return {"msg": response}
