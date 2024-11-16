from fastapi import APIRouter, Depends
from db.db_setup import get_session
from schemes.company import CreateCompanyScheme, CompanyResponseScheme
from utils.company import create_company_func, add_admin_func
from security.auth import get_current_user

company_router = APIRouter()


@company_router.post('/create-company', response_model=CompanyResponseScheme)
async def create_company_path(company_data: CreateCompanyScheme, current_user = Depends(get_current_user), session = Depends(get_session)):
    return await create_company_func(company_data, current_user['id'], session)


@company_router.patch('/add-admin')
async def add_admin_path(company_id: int, new_admin_id: int, current_user = Depends(get_current_user), session = Depends(get_session)):
    return await add_admin_func(company_id, new_admin_id, current_user['id'], session)
