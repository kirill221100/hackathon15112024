from pydantic import BaseModel
from schemes.user import UserResponseScheme
from typing import List

class CreateCompanyScheme(BaseModel):
    name: str

class CompanyResponseScheme(BaseModel):
    id: int
    name: str
    admins: List[UserResponseScheme]