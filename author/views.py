"""Author views."""

from flask_blog import app
from flask import render_template, redirect
from author.form import RegisterForm


@app.route('/login')
def login():
    """Homepage for user."""
    return 'Hello, user!'


@app.route('/register', methods=('GET', 'POST'))
def register():
    """Register form."""
    form = RegisterForm()
    return render_template('author/register.html', form=form)
