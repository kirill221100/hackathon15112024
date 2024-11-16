from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from schemes.auth import AuthDataScheme
from sqlalchemy.ext.asyncio import AsyncSession
from db.utils.user import get_user_by_email
#from security.email import send_email_verification, send_login_email
from security.jwt import create_access_token
from security.password import verify_pass


async def auth_func(auth_data: AuthDataScheme, session: AsyncSession):
    if user := await get_user_by_email(auth_data.email, session):
        if verify_pass(auth_data.password.get_secret_value(), user.hashed_password):
            data = {'user_id': user.id}
            return {'access_token': create_access_token(data),
                    'token_type': 'bearer'}
        raise HTTPException(400, 'Неправильный пароль')
    raise HTTPException(404, 'Нет такого пользователя')

