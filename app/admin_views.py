from flask_admin.contrib.sqla import ModelView

from app import admin, db
from app.models import User, Session


class MyModelView(ModelView):
    page_size = 50
    create_modal = True
    edit_modal = True


class UserView(MyModelView):
    # column_hide_backrefs = False
    column_list = ('email', 'first_name', 'surname')


class SessionView(MyModelView):
    column_list = (Session.date, Session.limit, 'users')
    # column_hide_backrefs = False


    # Flask Admin Views
admin.add_view(UserView(User, db.session))
admin.add_view(SessionView(Session, db.session))
