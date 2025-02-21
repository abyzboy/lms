from ..extensions import db, login_manager
from flask_login import UserMixin
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .course import Course

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    username : Mapped[str] = mapped_column(String(50), nullable=False)
    password : Mapped[str] = mapped_column(String(200), nullable=False)

    authored_courses  = relationship(Course, back_populates='author')
    
    courses = relationship(Course, secondary='user_course_association', back_populates='students') 