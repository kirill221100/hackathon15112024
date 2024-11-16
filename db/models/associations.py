from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from db.db_setup import Base

companies_users_association_table = Table(
    "companies_users_association_table",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("company_id", ForeignKey("companies.id"), primary_key=True),
)