import os
import secrets


class Config:
    """Base config."""

    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"


class ProdConfig(Config):
    """Production config."""

    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE_URI = os.getenv("PROD_DATABASE_URI")


class DevConfig(Config):
    """Development config."""

    DATABASE_URI = "sqlite:////tmp/foo.db"
    SECRET_KEY = secrets.token_hex()
    SQLALCHEMY_ECHO = True
