from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from itsdangerous import URLSafeTimedSerializer
from .config import Config

secret_key = Config.SECRET_KEY
serializer = URLSafeTimedSerializer(secret_key)
db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
migrate = Migrate()