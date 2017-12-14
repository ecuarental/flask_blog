"""Home views of the flask app."""

from flask_blog import app


@app.route('/')
@app.route('/index')
def index():
    """Homepage."""
    return "Hello World!"
