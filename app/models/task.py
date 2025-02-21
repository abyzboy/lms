from ..extensions import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Task(db.Model):
    id : Mapped[int] = mapped_column(Integer(), primary_key=True)
    title : Mapped[str] = mapped_column(String(50), nullable=False)
    desciption : Mapped[str] = mapped_column(String(400), nullable=False)
    answer : Mapped[str] = mapped_column(String(50), nullable=False)
    lesson_id : Mapped[int] = mapped_column(Integer(), ForeignKey('lesson.id'))

    lesson = relationship('Lesson', back_populates='tasks', uselist=False)