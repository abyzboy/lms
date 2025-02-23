from flask import Blueprint, redirect, url_for, flash
from flask_login import login_user, logout_user
from ..models.user import User
from ..extensions import db, serializer

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
        return redirect(url_for('main.index'))
    except Exception as e:
        print('Error:', e)
        return redirect(url_for('main.index'))

@user.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('main.index'))