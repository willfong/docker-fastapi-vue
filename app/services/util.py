import os
import jwt
import requests
import logging
import random
import string
from datetime import datetime, timedelta
from ..services import users


logger = logging.getLogger(__name__)
myFormatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(myFormatter)
logger.addHandler(handler)

SECRET_TOKEN = 'NEED_TO_FIND_A_GOOD_SECRET'

def create_token(sub):
    token = jwt.encode({
        'sub': sub,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=60*8)},
        secret_token())
    return token

def secret_token():
    # TODO: Obviously, this should be updated to AWS KMS
    return SECRET_TOKEN

def verify_token(token):  
    try: 
        response = jwt.decode(token, secret_token())
    except:
        logger.error(f'Bad token: {token}')
        return False
    return response

def token_to_userid(token):
    jwt = verify_token(token)
    if not jwt:
        return False
    return users.lookup(jwt.get('sub')).get('id')