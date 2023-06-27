from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# from settings import Config

metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

app = Flask(__name__, instance_relative_config=True)
# Load the default configuration
app.config.from_object("config.Config")

# Load the configuration from the instance folder
app.config.from_pyfile("config.py")

bootstrap = Bootstrap(app)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "auth.login"
login.login_message = "Please log in to access this page"

from . import auth, errors

app.register_blueprint(errors.bp)
app.register_blueprint(auth.bp)

from . import api_views, cli_commands, views  # noqa
