from fastapi import APIRouter, Depends
from db.db_setup import get_session
from utils.vacancy import create_vacancy_func
from schemes.vacancy import CreateVacancyScheme

vacancy_router = APIRouter()

@vacancy_router.post('/create-vacancy')
async def create_vacancy_path(vacancy_data: CreateVacancyScheme, session = Depends(get_session)):
    return await create_vacancy_func(vacancy_data, session)