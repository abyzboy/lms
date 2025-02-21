from ..extensions import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class UserCourseAssociation(db.Model):
    user_id : Mapped[int] = mapped_column(Integer(), ForeignKey('user.id'), primary_key=True)
    course_id : Mapped[int] = mapped_column(Integer(), ForeignKey('course.id'), primary_key=True)