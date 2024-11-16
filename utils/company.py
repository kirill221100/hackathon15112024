from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.utils.company import create_company, get_company_by_id_with_admins, add_admin
from db.utils.user import get_user_by_id
from schemes.company import CreateCompanyScheme


async def create_company_func(company_data: CreateCompanyScheme, user_id: int, session: AsyncSession):
    return await create_company(company_data, user_id, session)


async def add_admin_func(company_id: int, new_admin_id: int, user_id: int, session: AsyncSession):
    admin = await get_user_by_id(user_id, session)
    company = await get_company_by_id_with_admins(company_id, session)
    if admin in company.admins:
        new_admin = await get_user_by_id(new_admin_id, session)
        if new_admin not in company.admins:
            return await add_admin(new_admin, company, session)
        raise HTTPException(400, 'Пользователь, которого вы хотите сделать админом уже является им')
    raise HTTPException(400, 'Вы не являетесь админом этой компании')
