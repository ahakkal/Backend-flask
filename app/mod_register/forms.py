from flask.ext.wtf import Form

from wtforms import TextField, PasswordField

from wtforms.validators import Required, Email, EqualTo

class SignupForm(Form):
    firstname= TextField('Prenom client',[Required(message = 'Provide your firstname')])
    lastname= TextField('Nom client',[Required(message = 'Provide your lastname')])
    email = TextField('Email Address', [Email(),
                                        Required(message='Provide your email?')])
    password1 = PasswordField('Password', [Required(message='Must provide a password EqualTo')])
    password2=PasswordField('Confirm password', [Required(message='Passwords must match')])


