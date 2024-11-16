from fastapi import APIRouter, Depends
from db.db_setup import get_session
from utils.team import compatibility_between_two_candidates_func
from security.auth import get_current_user

team_router = APIRouter()


@team_router.get('/compatibility-between-two-candidates')
async def compatibility_between_two_candidates_path(first_candidate_id: int, second_candidate_id: int,
                                                   session = Depends(get_session)):
    return await compatibility_between_two_candidates_func(first_candidate_id, second_candidate_id, session)