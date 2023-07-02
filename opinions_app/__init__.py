from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from config import Config

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

db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
login = LoginManager()
login.login_view = "auth.login"
login.login_message = "Please log in to access this page"
bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    # Load the default configuration
    app.config.from_object(config_class)

    # Load the configuration from the instance folder
    try:
        app.config.from_pyfile("config.py")
    except:
        pass

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap.init_app(app)

    with app.app_context():
        from . import auth, errors

        app.register_blueprint(errors.bp)
        app.register_blueprint(auth.bp)

        from . import api_views, cli_commands, views  # noqa

    return app
