"""Creates the Flask application."""

from flask import Flask

app = Flask(__name__)
app.config.from_object('settings')

from home import views # noqa
