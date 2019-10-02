from flask import render_template, redirect, url_for, flash

from app import app, db
from app.forms import BookSessionForm
from app.models import Session, User


# TODO: route logic needs tidying up
@app.route('/', methods=['GET', 'POST'])
def index():
    form = BookSessionForm()
    next_session = Session.query.order_by(Session.date.desc()).first()
    new_user = False
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # User already exists
        if user:
            if user in next_session.users:
                flash(
                    f"Hey {user.first_name}, you have already booked for this session.")
            else:
                if next_session.spaces > 0:
                    next_session.users.append(user)
                    db.session.commit()
                    flash(f"Thanks {user.first_name}, you're booked in!")
                else:
                    flash(f'Sorry {user.first_name}, the session is full!')
            return redirect(url_for('index'))
        # User doesn't exist
        if form.first_name.data and form.surname.data:
            user = User(first_name=form.first_name.data,
                        surname=form.surname.data, email=form.email.data)
            db.session.add(user)
            if next_session.spaces > 0:
                next_session.users.append(user)
                flash(f"Thanks {user.first_name}, you're booked in!")
            else:
                flash(f'Sorry {user.first_name}, the session is full!')
            db.session.commit()
            return redirect(url_for('index'))
        new_user = True

    # TODO: next session wont always be most recent in time
    return render_template("index.html.j2", form=form, next_session=next_session, new_user=new_user)
