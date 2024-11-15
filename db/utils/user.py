from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, Session
from db.models.user import User
from fastapi import HTTPException
from pydantic import EmailStr
import datetime
from typing import List
from schemes.registration import RegisterScheme
from security.password import hash_password


async def get_user_by_username(username: str, session: AsyncSession):
    return (await session.execute(select(User).filter_by(username=username))).scalar_one_or_none()


async def get_user_by_email(email: EmailStr, session: AsyncSession):
    return (await session.execute(select(User).filter_by(email=email))).scalar_one_or_none()


async def get_user_by_id(user_id: int, session: AsyncSession):
    return (await session.execute(select(User).filter_by(id=user_id))).scalar_one_or_none()


async def get_user_by_id_with_chats(user_id: int, session: AsyncSession):
    return (await session.execute(select(User).filter_by(id=user_id)
                                  .options(selectinload(User.chats)))).scalar_one_or_none()


async def get_users_by_ids_with_chats(ids: List[int], session: AsyncSession):
    return (await session.execute(select(User).filter(User.id.in_(ids)))).scalars().all()


async def get_user_by_username_or_email(email: EmailStr, username: str, session: AsyncSession):
    return (await session.execute(select(User).filter(or_(User.username == username, User.email == email)))).scalar_one_or_none()

async def create_user(reg_data: RegisterScheme, session: AsyncSession):
    hashed_password = hash_password(reg_data.password.get_secret_value())
    print(reg_data.type.value)
    user = User(name=reg_data.name, surname=reg_data.surname, lastname=reg_data.lastname,
                hashed_password=hashed_password, birthday=reg_data.birthday, email=reg_data.email, phone=reg_data.phone,
                type=reg_data.type.value)
    session.add(user)
    await session.commit()
    return user


# async def reg_edit_user(data, session: AsyncSession):
#     if user := await get_user_by_id(data.id, session):
#         for k, v in data:
#             if v is not None and k != 'id':
#                 setattr(user, k, v)
#         await session.commit()
#         return user
#     raise HTTPException(404, 'user is not found')
#
#
# async def edit_profile(data: EditUserScheme, user_id: int, session: AsyncSession):
#     user = await get_user_by_id(user_id, session)
#     for k, v in data:
#         if v is not None and k not in ['avatar', 'username']:
#             setattr(user, k, v)
#     if data.username and await get_user_by_username(data.username, session):
#         raise HTTPException(409, "Username already exists")
#     elif data.username and data.username != 'string':
#         user.username = data.username
#     if data.avatar and data.avatar != 'string':
#         avatar = await upload_avatar(data.avatar, user_id, 'user')
#         user.avatar = avatar
#     await session.commit()
#     return user
#
#
# async def set_new_email(user_id: int, email: str, session: AsyncSession):
#     user = await get_user_by_id(user_id, session)
#     user.email = email
#     await session.commit()

