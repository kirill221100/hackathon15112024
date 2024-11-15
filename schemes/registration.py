import datetime
from enum import Enum
from pydantic import BaseModel, EmailStr, StringConstraints, model_validator, PastDate, Field, SecretStr
from typing import Annotated, Optional
from dateutil.relativedelta import relativedelta


class UserType(Enum):
    RECRUITER = 'recruiter'
    EMPLOYEE = 'employee'
    MANAGER = 'manager'
    CANDIDATE = 'candidate'

class RegisterScheme(BaseModel):
    name: str
    surname: str
    lastname: Optional[str] = None
    password: SecretStr = Field(min_length=6, max_length=32)
    email: EmailStr
    phone: Annotated[str, StringConstraints(min_length=12, max_length=12)]
    birthday: PastDate
    type: UserType

    @model_validator(mode='after')
    @classmethod
    def validate_data(cls, field_values):
        assert field_values.birthday + relativedelta(years=18) < datetime.date.today(), 'Меньше 18 лет'
        assert field_values.phone[:2] == '+7', 'Не русский номер'
        return field_values


