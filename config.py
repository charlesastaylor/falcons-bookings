import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Admin
    FLASK_ADMIN_SWATCH = 'slate'

    # Flask-Security
    SECURITY_PASSWORD_SALT = os.environ.get('SALT') or 'super-secret-salt'
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = False
    # fixes bug with flask security. ref https://github.com/mattupstate/flask-security/issues/685#ref-commit-241acf2
    SECURITY_EMAIL_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'debug'
    SECURITY_MSG_INVALID_PASSWORD = ("Invalid username or password", "error")
    SECURITY_MSG_PASSWORD_NOT_PROVIDED = (
        "Invalid username or password", "error")
    SECURITY_MSG_USER_DOES_NOT_EXIST = (
        "Invalid username or password", "error")

    # Flask-Mail
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'localhost'
    MAIL_PORT = int(os.environ.get('MAIL_PORT')) or 8025
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or None
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or None
