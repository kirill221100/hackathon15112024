from pydantic import EmailStr
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from db.models.employee import Employee
from utils.tarot import calculate_arcana, arcana
from schemes.employee import CreateEmployeeScheme



async def get_employee_by_id(user_id: int, session: AsyncSession):
    return (await session.execute(select(Employee).filter_by(id=user_id))).scalar_one_or_none()

async def get_employee_by_email(email: EmailStr, session: AsyncSession):
    return (await session.execute(select(Employee).filter_by(email=email))).scalar_one_or_none()


async def create_employee(employee_data: CreateEmployeeScheme, session: AsyncSession):
    arcana_num = calculate_arcana(employee_data.birthday.day, employee_data.birthday.month, employee_data.birthday.year)
    employee = Employee(name=employee_data.name, surname=employee_data.surname, lastname=employee_data.lastname,
                        birthday=employee_data.birthday, email=employee_data.email, phone=employee_data.phone,
                        arcana_num=arcana_num, arcana_name=arcana[arcana_num])
    session.add(employee)
    await session.commit()
    return employee
