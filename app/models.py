from datetime import datetime

from flask_security import UserMixin, RoleMixin

from app import db


# TODO: Should probably be called users_sessions
users = db.Table('users', db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                 db.Column('session_id', db.Integer, db.ForeignKey('session.id'), primary_key=True))

users_roles = db.Table('users_roles',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),  # nopep8
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    # Required by flask security columns
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return f'<Role {self.name}>'


class User(db.Model, UserMixin):
    # Required by flask security columns
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=users_roles,
                            backref=db.backref('users', lazy='dynamic'))
    # Additional columns
    first_name = db.Column(db.String(32))
    surname = db.Column(db.String(32))

    def __repr__(self):
        return f'<User {self.email}>'


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, index=True, unique=True)
    users = db.relationship('User', secondary=users, lazy='subquery',
                            backref=db.backref('sessions', lazy=True))
    limit = db.Column(db.Integer)

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
