"""Creates the Flask application."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

from blog import views # noqa
from author import views # noqa
