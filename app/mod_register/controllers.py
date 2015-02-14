from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from werkzeug import check_password_hash, generate_password_hash

from app import db

from app.mod_register.forms import SignupForm

from app.mod_auth.models import CLIENT
from werkzeug.security import generate_password_hash, check_password_hash

mod_register = Blueprint('register', __name__, url_prefix='/register')

@mod_register.route('/signup/', methods=['GET', 'POST'])
def register():
    form = SignupForm()
    print '<validate %d>' % form.validate_on_submit()
    if form.validate_on_submit() == 0:
        print 'lozoekjn'
        return render_template("register/signup.html", form=form)
    print '<password1 %s>' % form.password1.data
    
    user = CLIENT(email=form.email.data,
                          firstname=form.firstname.data,
                          lastname=form.lastname.data,
                          passwd=form.password1.data)
    db.session.add(user)
    db.session.commit()
        #token = user.generate_confirmation_token()
        #send_email(user.email, 'Confirm Your Account', 'auth/email/confirm', user=user, token=token)
        #flash('A confirmation email has been sent to you by email.')
    print 'lkef jbz'
    return redirect(url_for('auth.signin'))