from datetime import datetime

from flask import render_template, redirect, url_for, flash, abort
from flask_security import login_required, current_user

from app import app, db
from app.forms import BookSessionForm
from app.models import Session, User


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

# TODO: route logic needs tidying up
@app.route('/', methods=['GET', 'POST'])
def index():
    next_session = Session.next_session()
    form = BookSessionForm(session_id=next_session.id) if next_session else None  # nopep8
    return render_template("index.html.j2", form=form, next_session=next_session)


@app.route('/book', methods=['POST'])
@login_required
def book_session():
    form = BookSessionForm()
    if form.validate_on_submit():
        session = Session.query.get_or_404(int(form.session_id.data))
        if form.submit.data:
            if session.book(current_user):
                flash(f"Thanks {current_user.first_name}, you're booked in!")
            else:
                # TODO why did booking fail?
                flash(f"Failed to book")
            return redirect(url_for('index'))
        elif form.cancel.data:
            if session.cancel(current_user):
                flash(f"Your booking has been cancelled {current_user.first_name}.")  # nopep8
            else:
                flash("Failed to cancel")
            return redirect(url_for('index'))
    # TODO: handle
    abort(500)


@app.route('/profile')
@login_required
def user_profile():
    return render_template('profile.html.j2')
