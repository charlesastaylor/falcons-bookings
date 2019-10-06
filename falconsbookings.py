import click
from flask.cli import AppGroup

from app import app, db, user_datastore
from app.models import User, Role, Session, UserSession


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Session': Session, 'UserSession': UserSession, 'Role': Role, 'user_datastore': user_datastore}


setup_cli = AppGroup('setup')


@setup_cli.command('roles')
def setup_roles():
    pass
    # moved this functionaliy to before first request, left boiler plate for future cli commands


app.cli.add_command(setup_cli)
