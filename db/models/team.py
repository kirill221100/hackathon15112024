from db.db_setup import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, String, ForeignKey
from typing import List
import datetime



class Team(Base):
    __tablename__ = 'teams'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    desc: Mapped[str] = mapped_column(nullable=False)
    company_id: Mapped[int] = mapped_column(ForeignKey('companies.id'), nullable=False)
    company: Mapped["Company"] = relationship(foreign_keys=[company_id])
    employees: Mapped[List["Employee"]] = relationship(back_populates="team")
