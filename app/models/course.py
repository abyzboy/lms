from ..extensions import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Course(db.Model):
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    title : Mapped[str] = mapped_column(String(60), nullable=False)
    description : Mapped[str] = mapped_column(String(150))
    author_id : Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
    author = relationship('User', back_populates='authored_courses', uselist=False) # type: ignore
    lessons = relationship('Lesson', back_populates='course')
    students = relationship('User', secondary='user_course_association', back_populates='courses') # type: ignore
