import os

APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
SECRET_KEY = 'DeaDBeeF4012sudormrf@#$%^6324'
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
