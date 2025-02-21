from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from ..extensions import bcrypt
from ..models.user import User
from ..extensions import db
from ..forms import RegistrationForm

main = Blueprint('main', __name__)

@main.route('/', methods=['POST', 'GET'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password, email=form.email.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('Успешная регистрация')
            login_user(user)
        except Exception as e:
            flash(f'Ошибка {str(e)}')
        return render_template('main/home.html', form=form)
    return render_template('main/home.html', form=form)

@main.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect('/')