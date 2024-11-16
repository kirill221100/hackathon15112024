from db.db_setup import get_session
from fastapi import Depends
from db.utils.candidate import get_candidate_by_id
from utils.tarot import calculate_compatibility_between_two_people


async def compatibility_between_two_candidates_func(first_candidate_id: int, second_candidate_id: int,
                                                   session = Depends(get_session)):
    first_arcana = (await get_candidate_by_id(first_candidate_id, session)).arcana_num
    second_arcana = (await get_candidate_by_id(second_candidate_id, session)).arcana_num
    return calculate_compatibility_between_two_people(first_arcana, second_arcana)