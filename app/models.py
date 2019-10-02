from app import db


users = db.Table('users', db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                 db.Column('session_id', db.Integer, db.ForeignKey('session.id'), primary_key=True))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32))
    surname = db.Column(db.String(32))
    email = db.Column(db.String(120), index=True, unique=True)

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
