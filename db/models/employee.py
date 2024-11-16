from db.db_setup import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, String, ForeignKey
from typing import List
import datetime

from db.models.team import Team


class Employee(Base):
    __tablename__ = 'employees'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=True)
    birthday: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(unique=True, nullable=False)
    arcana_num: Mapped[int] = mapped_column(nullable=False)
    arcana_name: Mapped[str] = mapped_column(nullable=False)
    company_id: Mapped[int] = mapped_column(ForeignKey('companies.id'), nullable=False)
    company: Mapped["Company"] = relationship(foreign_keys=[company_id])
    team_id: Mapped[int] = mapped_column(ForeignKey('teams.id'), nullable=False)
    team: Mapped[Team] = relationship(foreign_keys=[team_id])
    role: Mapped[str] = mapped_column(nullable=False)
