from ..extensions import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Lesson(db.Model):
    id : Mapped[int] = mapped_column(Integer(), primary_key=True)
    title : Mapped[str] = mapped_column(String(50), nullable=False)

    videos = relationship('Video', back_populates='lesson', uselist=True)
    tasks = relationship('Task', back_populates='lesson', uselist=True)
 
    course_id : Mapped[int] = mapped_column(Integer(), ForeignKey('course.id'))
    course  = relationship('Course', back_populates='lessons', uselist=False)