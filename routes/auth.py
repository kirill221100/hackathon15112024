from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from schemes.auth import AuthDataScheme, AuthResponseScheme
from utils.auth import auth_func
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_setup import get_session
from db.utils.user import get_user_by_id, get_user_by_email
from security.jwt import create_access_token
from config import config

auth_router = APIRouter()


@auth_router.post('/auth', response_model=AuthResponseScheme)
async def auth_path(auth_data: AuthDataScheme, session: AsyncSession = Depends(get_session)):
    return await auth_func(auth_data, session)


@auth_router.post('/login-for-debug')
async def login_for_debug_path(login_data: OAuth2PasswordRequestForm = Depends(),
                               session: AsyncSession = Depends(get_session)):
    """вводить только username"""
    if config.DEBUG:
        user = await get_user_by_email(login_data.username, session)
        data = {'id': user.id}
        return {'access_token': create_access_token(data), 'token_type': 'bearer'}
    raise HTTPException(404)
