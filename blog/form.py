"""Blog Form."""

from wtforms import StringField, validators
from author.form import RegisterForm


class SetupForm(RegisterForm):
    """Blog Form Class definition."""

    name = StringField('Blog name', [
        validators.Required(),
        validators.Length(max=80)
    ])
