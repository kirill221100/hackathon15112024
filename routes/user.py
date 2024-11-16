from fastapi import APIRouter, Depends
from db.db_setup import get_session
from db.utils.user import get_user_by_id
from security.auth import get_current_user

user_router = APIRouter()


# @user_router.get('/me', response_model=ProfileResponseScheme)
# async def me_path(current_user = Depends(get_current_user), session = Depends(get_session)):
#     return await get_user_by_id(current_user['id'], session)
