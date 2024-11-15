from jose import jwt, JWTError
from datetime import timedelta, datetime
from fastapi import HTTPException, WebSocketException
from config import config


def create_access_token(data: dict):
    exp = datetime.utcnow() + timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = data.copy()
    token.update({'exp': exp})
    return jwt.encode(token, config.JWT_SECRET_KEY, algorithm=config.ALGORITHM)


def verify_token(token: str):
    try:
        if user_data := jwt.decode(token, config.JWT_SECRET_KEY, algorithms=[config.ALGORITHM]):
            return user_data
        raise HTTPException(401, detail='empty access token', headers={"WWW-Authenticate": "Bearer"})
    except JWTError:
        raise HTTPException(401, detail='invalid access token', headers={"WWW-Authenticate": "Bearer"})


