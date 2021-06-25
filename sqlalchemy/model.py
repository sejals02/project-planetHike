"""Project hikeplanet

Part 1: Define Model Classes
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Human(db.Model):
    """Data model for a human."""

    __tablename__ = "humans"

    human_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100), nullable=False)


class Animal(db.Model):
    """Data model for an animal."""

    __tablename__ = "animals"
    animal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    human_id = db.Column(db.Integer), db.ForeignKey('humans.human_id')
    name = db.Column(db.String(50), nullable=False)
    animal_species = db.Column(db.String(25), nullable=False)
    birth_year = db.Column(db.Integer, nullable = True)

    humans = db.relationship('Human.human.id')


def connect_to_db(app):
        """Connect the database to our Flask app."""

        app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///animals"
        app.config["SQLALCHEMY_ECHO"] = False
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        db.app = app
        db.init_app(app)
        print("Connected to db!")


if __name__ == "__main__":
        from flask import Flask

        app = Flask(__name__)
        connect_to_db(app)