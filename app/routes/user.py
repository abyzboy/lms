from flask import Blueprint, redirect, url_for, flash, request, render_template
from flask_login import login_user, logout_user, current_user, login_required
from ..models.user import User
from ..extensions import db, serializer, bcrypt
from ..forms import LoginForm
from ..functions import email_sender
from ..config import Config
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

@login_required
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
        
@login_required
@user.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@login_required
@user.route('/menu', methods=['POST', 'GET'])
def menu():
    return render_template('user/menu.html')

@login_required
@user.route('/verificate', methods=['POST', 'GET'])
def verificate():
    user = User.query.get(current_user.id)
    ref_email = f"{Config.DOMAIN}/confirm/{serializer.dumps(user.email, salt='email-confirm')}"
    try:
        email_sender.send_email.apply_async(kwargs={'subject': 'Подтверждение', 'body' : ref_email, 'to_email' : user.email})
        flash('На вашу почту отправлено письмо', 'success')
    except Exception as e:
        flash('Произошла ошибка при отправке писма', str(e))
    return redirect(request.referrer) if request.referrer else redirect(url_for('main.home'))

