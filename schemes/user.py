import datetime
from schemes.registration import UserType
from pydantic import BaseModel, EmailStr


class ProfileResponseScheme(BaseModel):
    id: int
    name: str
    surname: str
    lastname: str
    birthday: datetime.date
    phone: str
    email: EmailStr
    type: UserType