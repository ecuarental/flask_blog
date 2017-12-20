"""Author views."""

from flask_blog import app
from flask import render_template, redirect, url_for, session
from author.form import RegisterForm, LoginForm
from author.models import Author


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Homepage for user."""
    form = LoginForm()
    error = ""
    if form.validate_on_submit():
        author = Author.query.filter_by(
            username=form.username.data,
            password=form.password.data
        ).limit(1)
        if author.count():
            session['username'] = form.username.data
            return redirect(url_for('login_success'))
    return render_template('author/login.html', form=form, error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register form."""
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('author/register.html', form=form)


@app.route('/sucess')
def success():
    """Succesful Registration."""
    return "Succesful registration"


@app.route('/login_success')
def login_success():
    """Login Succesfully."""
    return "Author logged in!"
