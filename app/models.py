from datetime import datetime

from flask_security import UserMixin, RoleMixin

from app import db


# TODO: Should probably be called users_sessions
# TODO: Do need primary keys?
# users = db.Table('users', db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
#                  db.Column('session_id', db.Integer, db.ForeignKey('session.id'), primary_key=True))


users_roles = db.Table('users_roles',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),  # nopep8
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    # Columns required by flask security
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    @property
    def display_name(self):
        if self.name == "squad_1":
            return "1st Team"
        if self.name == "squad_2":
            return "2nd Team"
        return self.name

    def __repr__(self):
        return f'<Role {self.name}>'


class UserSession(db.Model):
    """Association class for many to many relationship between User and Session"""
    user_id = db.Column(db.Integer(), db.ForeignKey(
        'user.id'), primary_key=True)
    session_id = db.Column(db.Integer(), db.ForeignKey(
        'session.id'), primary_key=True)
    booked = db.Column(db.Boolean(), default=True)
    attended = db.Column(db.Boolean(), default=False)
    paid = db.Column(db.Boolean(), default=False)
    user = db.relationship('User', backref=db.backref('sessions', lazy=True))
    session = db.relationship(
        'Session', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f'<UserSession {self.user}-{self.session}>'


class User(db.Model, UserMixin):
    # Columns required by flask security
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=users_roles,
                            backref=db.backref('users', lazy='dynamic'))
    # Additional columns
    first_name = db.Column(db.String(32))
    surname = db.Column(db.String(32))
    credit = db.Column(db.Integer(), default=0)

    def __repr__(self):
        return f'<User {self.email}>'


def default_cost(u18=False):
    # TODO: Create Prices model for Session class gets default prices from
    # TODO: add new models for default prices and lookup instead of hardcoded
    return 4 if u18 else 6


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, index=True, unique=True)
    # users = db.relationship('User', secondary=users, lazy='subquery',
    #                         backref=db.backref('sessions', lazy=True))
    limit = db.Column(db.Integer)
    location = db.Column(db.String(255))
    cost = db.Column(db.Integer, default=default_cost())
    cost_u18 = db.Column(db.Integer, default=default_cost(u18=True))

    @property
    def spaces(self):
        assert self.limit is not None, "Session: No Limit set"
        return max(self.limit - len(self.users), 0)

    def __repr__(self):
        return f'<Session {self.date}>'

    @staticmethod
    def next_session():
        sessions = Session.query.order_by(Session.date.desc()).all()
        for i, s in enumerate(sessions):
            if s.date < datetime.now():
                if i == 0:
                    # Edge case - all sessions in past
                    return None
                else:
                    return sessions[i-1]
        # Edge case - all sessions in future
        return sessions[-1]
