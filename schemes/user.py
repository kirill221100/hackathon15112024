import datetime
from enum import Enum
from pydantic import BaseModel, EmailStr, StringConstraints, model_validator, PastDate, Field, SecretStr
from typing import Annotated, Optional
from dateutil.relativedelta import relativedelta


class UserType(Enum):
    #RECRUITER = 'recruiter'
    EMPLOYEE = 'employee'
    CANDIDATE = 'candidate'


class UserResponseScheme(BaseModel):
    id: int
    name: str
    surname: str
    lastname: str
    email: EmailStr