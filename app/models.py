# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime

class Movie_Properties(db.Model):

    _tablename_ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text(500))
    poster = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def _init_(self, title, description, poster, created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at