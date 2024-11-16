import datetime
from enum import Enum
from pydantic import BaseModel, EmailStr, StringConstraints, model_validator, PastDate, Field, SecretStr
from typing import Annotated, Optional
from dateutil.relativedelta import relativedelta

class CreateCandidateScheme(BaseModel):
    name: str
    surname: str
    lastname: Optional[str] = None
    email: EmailStr
    phone: Annotated[str, StringConstraints(min_length=12, max_length=12)]
    birthday: PastDate
    vacancy_id: int

    @model_validator(mode='after')
    @classmethod
    def validate_data(cls, field_values):
        assert field_values.birthday + relativedelta(years=18) < datetime.date.today(), 'Меньше 18 лет'
        assert field_values.phone[:2] == '+7', 'Не русский номер'
        return field_values