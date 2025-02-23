from flask import Flask
from .extensions import db
from .config import Config
from .extensions import db, migrate, login_manager
from .routes.main import main
from .routes.user import user
from .models.all_models import *

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    app.register_blueprint(user)
    app.register_blueprint(main)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    login_manager.login_message = "Вы не можете получить доступ к данной странице нужно сначало войти"

    with app.app_context():
        db.create_all()
    
    return app

    