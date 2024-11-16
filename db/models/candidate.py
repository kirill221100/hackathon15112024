from db.db_setup import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, String, ForeignKey
from typing import List
import datetime

from db.models.vacancy import Vacancy


class Candidate(Base):
    __tablename__ = 'candidates'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=True)
    birthday: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(unique=True, nullable=False)
    arcana_num: Mapped[int] = mapped_column(nullable=False)
    arcana_name: Mapped[str] = mapped_column(nullable=False)
    vacancy_id: Mapped[int] = mapped_column(ForeignKey('vacancies.id'), nullable=False)
    vacancy: Mapped[Vacancy] = relationship(foreign_keys=[vacancy_id])