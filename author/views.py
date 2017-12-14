"""Author views."""

from flask_blog import app


@app.route('/login')
def login():
    """Homepage for user."""
    return 'Hello, user!'
