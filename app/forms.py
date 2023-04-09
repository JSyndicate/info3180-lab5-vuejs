# Add any form classes for Flask-WTF here

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired])
    poster = FileField('Movie Poster', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])

