from pydantic import BaseModel, EmailStr, StringConstraints, model_validator, PastDate, Field, SecretStr
from typing import Optional


class RegisterScheme(BaseModel):
    name: str
    surname: str
    lastname: Optional[str] = None
    email: EmailStr
    password: SecretStr = Field(min_length=6, max_length=32)


