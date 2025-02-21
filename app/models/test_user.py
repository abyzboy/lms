from ..extensions import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class UserTest(db.Model):
    id : Mapped[int] = mapped_column(Integer(), primary_key=True)
    title : Mapped[str] = mapped_column(String(50), nullable=False)