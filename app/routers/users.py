from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from ..services import util, users

router = APIRouter()

class LoginToken(BaseModel):
    value: str

@router.post("/facebook")
def login_facebook(token: LoginToken):
    facebook_data = users.facebook_verify_access_token(token.value)
    if not facebook_data:
        raise HTTPException(status_code=403, detail="Invalid Facebook Token")
    user_id = users.find_or_create_user('facebook', facebook_data['id'], facebook_data)
    return {"token": util.create_login_token(user_id)}

@router.post("/google")
def login_google(token: LoginToken):
    google_data = users.google_verify_access_token(token.value)
    if not google_data:
        raise HTTPException(status_code=403, detail="Invalid Google Token")
    user_id = users.find_or_create_user('google', google_data['sub'], google_data)
    return {"token": util.create_login_token(user_id)}

@router.post("/test-account")
def login_test(username: LoginToken):
    user_id = users.find_or_create_user(f"test-account||{username.value}")
    util.logger.warning(f"Test Account Logged In: {user_id}")
    if not user_id:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    return {"token": util.create_token(user_id)}

@router.get("/lookup")
def lookup(id: str):
    return users.lookup(id)