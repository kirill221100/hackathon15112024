from db.db_setup import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, String, ForeignKey
from db.models.company import Company
from db.models.associations import companies_users_association_table
from typing import List
import datetime



class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=True)
    hashed_password: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    companies: Mapped[List[Company]] = relationship(back_populates="admins", secondary=companies_users_association_table)
