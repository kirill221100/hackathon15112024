from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.vacancy import Vacancy
from schemes.vacancy import CreateVacancyScheme


async def create_vacancy(vacancy_data: CreateVacancyScheme, session: AsyncSession):
    vacancy = Vacancy(title=vacancy_data.title, desc=vacancy_data.desc, company_id=vacancy_data.company_id)
    session.add(vacancy)
    await session.commit()
    return vacancy