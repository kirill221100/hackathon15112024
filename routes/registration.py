from fastapi import APIRouter, Depends
from schemes.registration import RegisterScheme
from utils.registration import registration_func
from db.db_setup import get_session
from sqlalchemy.ext.asyncio import AsyncSession

registration_router = APIRouter()


@registration_router.post('/', response_model=dict)
async def registration_path(reg_data: RegisterScheme, session: AsyncSession = Depends(get_session)):
    return await registration_func(reg_data, session)
