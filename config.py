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

    # Flask-Mail
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'localhost'
    MAIL_PORT = os.environ.get('MAIL_PORT') or 8025
