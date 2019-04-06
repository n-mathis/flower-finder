import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    UPLOAD_FOLDER = 'static/'
    LOC_MODELS_FOLDER = '/home/ubuntu/cs121/app/'
