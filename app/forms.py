from flask_wtf import FlaskForm
from flask_security.forms import RegisterForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email, NumberRange, InputRequired


class MyRegisterForm(RegisterForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])


class BookSessionForm(FlaskForm):
    session_id = HiddenField("session_id", validators=[InputRequired()])
    submit = SubmitField('Book')
    cancel = SubmitField('Cancel')
