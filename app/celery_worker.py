from celery import Celery
from flask import Flask

temp_app = Flask(__name__)

temp_app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
temp_app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(
    temp_app.import_name,
    backend=temp_app.config['CELERY_RESULT_BACKEND'],
    broker=temp_app.config['CELERY_BROKER_URL']
)
celery.conf.update(temp_app.config)