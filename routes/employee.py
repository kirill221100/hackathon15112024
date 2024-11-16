from fastapi import APIRouter, Depends
from db.db_setup import get_session
from utils.employee import create_employee_func
from schemes.employee import CreateEmployeeScheme

employee_router = APIRouter()

@employee_router.post('/create-employee')
async def create_employee_path(employee_data: CreateEmployeeScheme, session = Depends(get_session)):
    return await create_employee_func(employee_data, session)
