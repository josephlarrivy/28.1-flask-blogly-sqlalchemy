from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User (db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String)

    @property
    def full_name(self):
        """Return full name of user."""
        return f"{self.first_name} {self.last_name}"


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
