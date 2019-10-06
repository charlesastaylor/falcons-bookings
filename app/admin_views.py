from flask import redirect, url_for, request
from flask_security import current_user
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView

from app import admin, db
from app.models import User, Session, Role, UserSession


class SecuredAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        # if logged in but not admin redirect home
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        # otherwise redirect to login
        return redirect(url_for('security.login', next=request.url))


class SecuredModelView(ModelView):
    page_size = 50
    create_modal = True
    edit_modal = True

    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        # redirect to all admin views to base view for handling
        return redirect(url_for('admin.index'))


class UserView(SecuredModelView):
    # column_hide_backrefs = False
    column_list = ('email', 'first_name', 'surname', 'credit',
                   'roles', 'active', 'confirmed_at')

    # def is_accessible(self):
    #     return current_user.is_authenticated


class SessionView(SecuredModelView):
    column_list = (Session.date, Session.limit,
                   Session.location, 'users')
    # form_columns = ('date', 'limit', 'location',)
    # inline_models = ((UserSession, {
    #     'form_colums': ('id', 'user', 'booked', 'attended', 'paid',)
    # }),)


class RoleView(SecuredModelView):
    pass

    # Flask Admin Views
admin.add_view(UserView(User, db.session))
admin.add_view(SessionView(Session, db.session))
admin.add_view(RoleView(Role, db.session))
admin.add_view(SecuredModelView(UserSession, db.session))
