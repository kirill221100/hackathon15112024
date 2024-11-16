from db.db_setup import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, String
#from schemes.registration import UserType
from typing import List
import datetime

from db.models.associations import companies_users_association_table


class Company(Base):
    __tablename__ = 'companies'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    employees: Mapped[List["Employee"]] = relationship(back_populates="company")
    teams: Mapped[List["Team"]] = relationship(back_populates="company")
    vacancies: Mapped[List["Vacancy"]] = relationship(back_populates="company")
    admins: Mapped[List["User"]] = relationship(back_populates="companies", secondary=companies_users_association_table)
