"""Home views of the flask app."""

from flask_blog import app, db
from flask import render_template, redirect, flash, url_for
from blog.form import SetupForm
from author.models import Author
from blog.models import Blog
from author.decorators import login_required
import bcrypt


@app.route('/')
@app.route('/index')
def index():
    """Homepage."""
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))
    return "Hello World!"


@app.route("/admin")
@login_required
def admin():
    """Administration Form."""
    return render_template('blog/admin.html')


@app.route('/setup', methods=['GET', 'POST'])
def setup():
    """Define the setup form."""
    form = SetupForm()
    error = ""
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        author = Author(
            form.fullname.data,
            form.email.data,
            form.username.data,
            hashed_password,
            True
        )
        db.session.add(author)
        db.session.flush()
        if author.id:
            blog = Blog(
                form.name.data,
                author.id,
            )
            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = "Error creating user"
        if author.id and blog.id:
            db.session.commit()
            flash("Blog created")
            return redirect(url_for('admin'))
        else:
            db.session.rollback()
            error = "Error creating blog"

    return render_template('blog/setup.html', form=form, error=error)
