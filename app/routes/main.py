from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models.user import User
from ..extensions import db

main = Blueprint('main', __name__)

@main.route('/', methods=['POST', 'GET'])
def index():
    return '<p1>Hello</p1>'

@main.route('/test', methods=['POST', 'GET'])
def test():
    user = User(email='521', username='521', password='125')
    try:
        db.session.add(user)
        db.session.commit()
        return '<p1>Ok</p1>'
    except Exception as e:
            print('неудача')
    return '<p1>Not ok</p1>'