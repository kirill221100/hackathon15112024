from pydantic import BaseModel, EmailStr, SecretStr, Field
from typing import Optional

class AuthDataScheme(BaseModel):
    email: EmailStr
    password: SecretStr = Field(min_length=6, max_length=32)

class AuthResponseScheme(BaseModel):
    access_token: str
    token_type: str
