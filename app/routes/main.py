from flask import Blueprint, render_template, redirect, url_for, flash
from ..extensions import bcrypt
from ..models.user import User
from ..extensions import db, serializer
from ..forms import RegistrationForm
from ..functions import email_sender
from ..config import Config

main = Blueprint('main', __name__)

@main.route('/', methods=['POST', 'GET'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password, email=form.email.data)
        try:
            db.session.add(user)
            ref_email = f"{Config.DOMAIN}/confirm/{serializer.dumps(form.email.data, salt='email-confirm')}"
            email_sender.send_email.apply_async(kwargs={'subject': 'Подтверждение', 'body' : ref_email, 'to_email' : form.email.data})
            flash('На вашу почту отправлено письмо', 'success')
            db.session.commit()
        except Exception as e:
            flash(f'Ошибка {str(e)}')
        return render_template('main/home.html', form=form)
    return render_template('main/home.html', form=form)