from flask import Flask, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'auth.login'
login.login_message = lazy_gettext('Please log in to access this page')

mail = Mail(app)
moment = Moment(app)
babel = Babel(app)

from app import routes, models

from app.errors import bp as errors_bp
from app.auth import bp as auth_bp
app.register_blueprint(errors_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

