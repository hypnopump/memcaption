import os
_basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SECRET_KEY = 'dummy'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = True
DATABASE_CONNECT_OPTIONS = {}