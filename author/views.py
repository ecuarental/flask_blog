"""Author views."""

from flask_blog import app
from flask import render_template, redirect, url_for
from author.form import RegisterForm


@app.route('/login')
def login():
    """Homepage for user."""
    return 'Hello, user!'


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register form."""
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('sucess'))
    return render_template('author/register.html', form=form)


@app.route('/sucess')
def success():
    """Succesful Registration."""
    return "Succesful registration"
