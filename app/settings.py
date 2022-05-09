from os import environ

SECRET_KEY = environ.get("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = (
    environ.get("SQLALCHEMY_DATABASE_URI") or "sqlite:////tmp/test.db"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
