import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    secret_key = "jwaghgwaiurgahwoihgaw421"
    APPNAME = "app"
    ROOT = os.path.abspath(APPNAME)
    USER = os.environ.get('POSTGRES_USER')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    HOST = os.environ.get('POSTGRES_HOST')
    PORT = os.environ.get('POSTGRES_PORT')
    DB = os.environ.get('POSTGRES_DB')
    DOMAIN = "http://127.0.0.1:5000/"
    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:7777/{DB}'
    SECRET_KEY = 'sagjaw89gh21h83g2'
    SQLALCHEMY_TRACK_MODIFICATIONS = True