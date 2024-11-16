from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from db.models.company import Company
from db.models.user import User

from db.utils.user import get_user_by_id
from schemes.company import CreateCompanyScheme


async def get_company_by_id(company_id: int, session: AsyncSession):
    return (await session.execute(select(Company).filter_by(id=company_id))).scalar_one_or_none()


async def get_company_by_id_with_admins(company_id: int, session: AsyncSession):
    return (await session.execute(select(Company).filter_by(id=company_id).options(selectinload(Company.admins)))).scalar_one_or_none()


async def create_company(company_data: CreateCompanyScheme, user_id: int, session: AsyncSession):
    company = Company(name=company_data.name)
    user = await get_user_by_id(user_id, session)
    company.admins.append(user)
    session.add(company)
    await session.commit()
    return company


async def add_admin(new_admin: User, company: Company, session: AsyncSession):
    company.admins.append(new_admin)
    await session.commit()