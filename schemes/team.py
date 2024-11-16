from pydantic import BaseModel
from typing import List

class CreateTeamScheme(BaseModel):
    name: str
    company_id: int
    employees_ids: List[int]