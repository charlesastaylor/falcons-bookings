from flask import Flask, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin, AdminIndexView
from flask_security import Security, SQLAlchemyUserDatastore, current_user

from config import Config

# Set up Flask app
app = Flask(__name__)
app.config.from_object(Config)
# Set up Flask-SQLAlchemy
db = SQLAlchemy(app)
# Set up Flask-Migrate
migrate = Migrate(app, db)
# Set up Flask-Admin
admin = Admin(name='falcons bookings', template_mode='bootstrap3')
from app.admin_views import SecuredAdminIndexView  # nopep8
admin.init_app(app, index_view=SecuredAdminIndexView())
# Setup Flask-Security
from app.models import User, Role  # nopep8
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

from app import routes, models, admin_views  # nopep8
