from pydantic import EmailStr
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from db.models.candidate import Candidate
from schemes.candidate import CreateCandidateScheme
from utils.tarot import arcana, calculate_arcana


async def get_candidate_by_id(user_id: int, session: AsyncSession):
    return (await session.execute(select(Candidate).filter_by(id=user_id))).scalar_one_or_none()


async def get_candidate_by_email(email: EmailStr, session: AsyncSession):
    return (await session.execute(select(Candidate).filter_by(email=email))).scalar_one_or_none()


async def create_candidate(candidate_data: CreateCandidateScheme, session: AsyncSession):
    arcana_num = calculate_arcana(candidate_data.birthday.day, candidate_data.birthday.month, candidate_data.birthday.year)
    candidate = Candidate(name=candidate_data.name, surname=candidate_data.surname, lastname=candidate_data.lastname,
                          birthday=candidate_data.birthday, email=candidate_data.email, phone=candidate_data.phone,
                          arcana_num=arcana_num, arcana_name=arcana[arcana_num], vacancy_id=candidate_data.vacancy_id)
    session.add(candidate)
    await session.commit()
    return candidate
