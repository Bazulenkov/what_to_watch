from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# from settings import Config

app = Flask(__name__, instance_relative_config=True)
# Load the default configuration
app.config.from_object("config.Config")

# Load the configuration from the instance folder
app.config.from_pyfile("config.py")

# app.config.from_mapping()

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import api_views, cli_commands, error_handlers, views
