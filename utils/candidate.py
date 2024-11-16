from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemes.registration import RegisterScheme
from db.utils.candidate import create_candidate, get_candidate_by_email
from schemes.candidate import CreateCandidateScheme


async def create_candidate_func(candidate_data: CreateCandidateScheme, session: AsyncSession):
    if await get_candidate_by_email(candidate_data.email, session):
        raise HTTPException(status_code=409, detail="Кандидат с таким email уже есть")
    return await create_candidate(candidate_data, session)