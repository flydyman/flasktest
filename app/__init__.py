from flask import Flask, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext
from config import Config
from elasticsearch import Elasticsearch
import os

db = SQLAlchemy()
# db: SQLAlchemy
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = lazy_gettext('Please log in to access this page')

mail = Mail()
moment = Moment()
babel = Babel()

from app import models

from app.errors import bp as errors_bp
from app.auth import bp as auth_bp
from app.main import bp as main_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # db = app.config['DB_SERVER']()
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    babel.init_app(app)

    app.app_context().push()
    db.create_all()

    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(errors_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']])

    if app.config['FLASK_ENV'] == 'development':
        if os.system('pip freeze > req.txt'):
            raise RuntimeError('Cannot make req.txt')

    return app


    @babel.localeselector
    def get_locale():
        return request.accept_languages.best_match(app.config['LANGUAGES'])
