"""Blog Model."""
from flask_blog import db


class Blog(db.Model):
    """Blog Model Class."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    admin = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __init__(self, name, admin):
        """Initialize class object."""
        self.name = name
        self.admin = admin

    def __repr__(self):
        """Representation of the object."""
        return '<Blog %r>' % self.name
