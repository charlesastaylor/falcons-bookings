from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_security import Security, SQLAlchemyUserDatastore
from flask_mail import Mail

from config import Config

# Set up Flask app
app = Flask(__name__)
app.config.from_object(Config)
# Set up Flask-SQLAlchemy
db = SQLAlchemy(app)
# Set up Flask-Migrate
migrate = Migrate(app, db)
# Set up Flask-Mail
mail = Mail(app)
# Set up Flask-Admin
admin = Admin(name='falcons bookings', template_mode='bootstrap3')
from app.admin_views import SecuredAdminIndexView  # nopep8
admin.init_app(app, index_view=SecuredAdminIndexView())
# Setup Flask-Security
from app.models import User, Role  # nopep8
from app.forms import MyRegisterForm  # nopep8
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, register_form=MyRegisterForm)


@app.before_first_request
def setup_roles():
    default_roles = ['admin', 'member', 'squad_1', 'squad_2']
    for role in default_roles:
        user_datastore.find_or_create_role(role)
    db.session.commit()


from app import routes, models, admin_views  # nopep8
