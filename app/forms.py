from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email
from wtforms import StringField, PasswordField, SubmitField
from .models.user import User

class RegistrationForm(FlaskForm):
    username = StringField("ФИО", validators=[DataRequired(), Length(min=2, max=80)])
    email = StringField('Почта', validators=[DataRequired(), Email(message='Введите почту корректно')])
    password = PasswordField("Пароль", validators=[DataRequired(), Length(min=6, max=30)])
    confirm_password = PasswordField("Подтвердите пароль", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Зарегистрироваться")
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Данная почта уже занята. Пожалуйста, выберите другое...")
        
class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired(), Email(message='Введите почту корректно')])
    password = PasswordField("Пароль", validators=[DataRequired(), Length(min=6, max=30)])
    submit = SubmitField("Войти")
        