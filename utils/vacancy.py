from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.utils.vacancy import create_vacancy
from schemes.vacancy import CreateVacancyScheme


async def create_vacancy_func(vacancy_data: CreateVacancyScheme, session: AsyncSession):
    return await create_vacancy(vacancy_data, session)