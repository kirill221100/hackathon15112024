from db.db_setup import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, String, ForeignKey
#from schemes.registration import UserType
from typing import List
import datetime


class Vacancy(Base):
    __tablename__ = 'vacancies'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    desc: Mapped[str] = mapped_column(nullable=False)
    company_id: Mapped[int] = mapped_column(ForeignKey('companies.id'), nullable=False)
    company: Mapped["Company"] = relationship(foreign_keys=[company_id])
    candidates: Mapped[List["Candidate"]] = relationship(back_populates='vacancy')
