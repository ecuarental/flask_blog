"""Home views of the flask app."""

from flask_blog import app, db
from flask import render_template, redirect, flash, url_for
from blog.form import SetupForm
from author.models import Author
from blog.models import Blog


@app.route('/')
@app.route('/index')
def index():
    """Homepage."""
    return "Hello World!"


@app.route("/admin")
def admin():
    """Administration Form."""
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))
    return render_template('blog/admin.html')


@app.route('/setup')
def setup():
    """Define the setup form."""
    form = SetupForm()
    return render_template('blog/setup.html', form=form)
