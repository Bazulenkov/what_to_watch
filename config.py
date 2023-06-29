import os
import secrets


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///db.sqlite3")
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex())
