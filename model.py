"""Project planethike

Part 1: Define Model Classes
"""

from sqlalchemy.orm import backref
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Stores information about each user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, 
                                    primary_key=True, 
                                    autoincrement=True)
    fname = db.Column(db.String(100), nullable=True)
    lname = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    trails = db.relationship('Trail')
    hikes = db.relationship('Hike', secondary='trails', backref='users')


class Hike(db.Model):
    """Stores information for each hiking place."""

    __tablename__ = "hikes"

    hike_id = db.Column(db.Integer, 
                                    primary_key=True, 
                                    autoincrement=True)
    name = db.Column(db.String, nullable=False)
    area_name = db.Column(db.String, nullable=False)
    city_name = db.Column(db.String, nullable=False)
    state_name = db.Column(db.String, nullable=False)
    country_name = db.Column(db.String, nullable=False)
    geoloc = db.Column(db.String, nullable=False)
    difficulty_level = db.Column(db.String, nullable=False)
    miles = db.Column(db.Float, nullable=False)
    features = db.Column(db.String)
    avg_rating = db.Column(db.Float)

    #users = db.relationship('User')
    trails = db.relationship('Trail')
 
class Trail(db.Model):
    """saves hike data for a given user"""

    __tablename__ = "trails"

    trail_id = db.Column(db.Integer, 
                                    primary_key=True, 
                                    autoincrement=True)
    hike_id = db.Column(db.Integer, db.ForeignKey('hikes.hike_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    users = db.relationship('User')
    hikes = db.relationship('Hike')

    # hike = db.relationship('Hike', backref='trails')
    # user = db.relationship('User', backref='trails')

def connect_to_db(app):
        """Connect the database to our Flask app."""

        app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///hikeplanet"
        app.config["SQLALCHEMY_ECHO"] = False
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        db.app = app
        db.init_app(app)
        print("Connected to db!")


if __name__ == "__main__":
        from flask import Flask

        app = Flask(__name__)
        connect_to_db(app)