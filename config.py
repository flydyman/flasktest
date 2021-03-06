import os
from flaskext.mysql import MySQL

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    FLASK_APP = 'app.py'
    FLASK_ENV = 'development'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ojhyf;gdf;ldksfpgorkegdfkjlkgsdgkjdshurmnalweunsa;o237'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'mysql+mysqlconnector://pythoner:pythoner@localhost:3306/flask_db01?charset=utf8'# 'sqlite:///{}'.format(os.path.join(basedir, 'db.sqlite'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL') or 'http://localhost:9200'
    # email section
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'localhost'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 8025)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None or 0
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or None
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or None
    ADMINS = ['flydeadmanbrest@gmail.com']
    LANGUAGES = ['en', 'ru']

