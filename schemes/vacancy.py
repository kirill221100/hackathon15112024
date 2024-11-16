from pydantic import BaseModel

class CreateVacancyScheme(BaseModel):
    title: str
    desc: str
    company_id: int