from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from werkzeug import check_password_hash, generate_password_hash

from app import db

from app.mod_auth.forms import LoginForm

from app.mod_auth.models import CLIENT

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

@mod_auth.route('/signin/', methods=['GET', 'POST'])

def signin():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = CLIENT.query.filter_by(ADRESSE_MAIL=form.email.data).first()
        if user and user.check_password(form.password.data):
            #session['user_id'] = user.id
                flash('Welcome %s'% user.PRENOM_CLIENT)
                print 'laoli binajah'
                return render_template("/auth/laloli.html")
        flash('Wrong email or password', 'error-message')
    print 'l3alali'
    return render_template("/auth/signin.html", form=form)

@mod_auth.route('/auth/index')
def laloli():
    return laloli.html