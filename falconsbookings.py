import click
from flask_mail import Message
from flask.cli import AppGroup

from app import app, db, user_datastore, mail
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


@app.cli.command('mail-server')
def start_mail_server():
    import smtpd
    import asyncore
    server = smtpd.DebuggingServer(('localhost', 8025), None)
    print("Debug smtpd mail server started")
    asyncore.loop()


@app.cli.command('mail-test')
def send_test_email():
    msg = Message("Hello",
                  sender="from@example.com",
                  recipients=["charlesastaylor@gmail.com"])
    msg.body = "Testing 1 2 3"
    mail.send(msg)
