"""Author Forms."""

from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField


class RegisterForm(Form):
    """Register Form."""

    fullname = StringField('Full Name', [validators.Required()])
    email = EmailField('Email', [validators.Required()])
    username = StringField('Username', [
        validators.Required(),
        validators.Length(min=4, max=25)
    ])
    password = PasswordField('New password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=4, max=80)
    ])
    confirm = PasswordField('Repeat password')


class LoginForm(Form):
    """Login Form class definition."""

    username = StringField('Username', [
        validators.Required(),
        validators.Length(min=4, max=25)
    ])
    password = PasswordField('Password', [
        validators.Required(),
        validators.Length(min=4, max=80)
    ])
