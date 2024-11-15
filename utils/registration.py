from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemes.registration import RegisterScheme
from db.utils.user import get_user_by_email, create_user


async def registration_func(reg_data: RegisterScheme, session: AsyncSession):
    print(reg_data)
    if await get_user_by_email(reg_data.email, session):
        raise HTTPException(status_code=409, detail="Email уже зарегистрирован")
    await create_user(reg_data, session)
    return {'msg': 'Вы зарегистрировали аккаунт! Теперь авторизуйтесь.'}
