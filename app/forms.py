from flask_wtf import FlaskForm
from flask_security.forms import RegisterForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class MyRegisterForm(RegisterForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])


class BookSessionForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name')
    surname = StringField('Surname')
    submit = SubmitField('Book')
