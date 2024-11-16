from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemes.registration import RegisterScheme
from db.utils.employee import create_employee, get_employee_by_email
from schemes.employee import CreateEmployeeScheme


async def create_employee_func(employee_data: CreateEmployeeScheme, session: AsyncSession):
    if await get_employee_by_email(employee_data.email, session):
        raise HTTPException(status_code=409, detail="Сотрудник с таким email уже есть")
    await create_employee(employee_data, session)