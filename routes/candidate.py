from fastapi import APIRouter, Depends
from db.db_setup import get_session
from utils.candidate import create_candidate_func
from schemes.candidate import CreateCandidateScheme

candidate_router = APIRouter()

@candidate_router.post('/create-candidate')
async def create_candidate_path(candidate_data: CreateCandidateScheme, session = Depends(get_session)):
    return await create_candidate_func(candidate_data, session)
