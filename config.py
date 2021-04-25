import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ojhyf;gdf;ldksfpgorkegdfkjlkgsdgkjdshurmnalweunsa;o237'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///{}'.format(os.path.join(basedir, 'db.sqlite'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

