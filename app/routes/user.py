from flask import Blueprint, redirect, url_for, flash, request, render_template
from flask_login import login_user, logout_user
from ..models.user import User
from ..extensions import db, serializer, bcrypt
from ..forms import LoginForm

user = Blueprint('user', __name__)

@user.route('/confirm/<token>', methods=['POST', 'GET'])
def confirm_email(token, expiration=3600):
    try:
        email = serializer.loads(token, salt='email-confirm', max_age=expiration)
        user = db.session.query(User).filter(User.email == email).first()
        user.is_verified = True
        db.session.commit()
        login_user(user)
        flash('Вы успешно авторизовали свою почту', "success")
        return redirect(url_for('main.home'))
    except Exception as e:
        print('Error:', e)
        return redirect(url_for('main.home'))

@user.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Ошибка входа. Проверьте email или пароль', 'danger')
    
    return render_template('user/login.html', form=form)
        

@user.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('main.home'))