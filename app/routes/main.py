from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, current_user
from ..extensions import bcrypt
from ..models.user import User
from ..extensions import db
from ..forms import RegistrationForm

main = Blueprint('main', __name__)

@main.route('/', methods=['POST', 'GET'])
def home():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password, email=form.email.data)
        try:
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            return redirect(url_for('user.verificate'))
        except Exception as e:
            flash(f'Ошибка {str(e)}')
        return render_template('main/home.html', form=form)
    return render_template('main/home.html', form=form)