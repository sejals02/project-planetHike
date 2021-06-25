"""CRUD operations."""

from model import db, User, Hike, Trail, connect_to_db
import server


def create_user(fname, lname, email, password):
    """Create and return a new user."""

    user = User(fname=fname, lname=lname, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_hike(name, area_name, city_name, state_name, country_name, geoloc, difficulty_level, miles, features, avg_rating):
    """seeded and returned a new hike."""

    hike = Hike(
        name=name,
        area_name=area_name,
        city_name=city_name,
        state_name=state_name,
        country_name=country_name,
        geoloc=geoloc,
        difficulty_level=difficulty_level,
        miles=miles,
        features=features,
        avg_rating=avg_rating
    )

    db.session.add(hike)
    db.session.commit()

    return hike


def create_trail(user_id, hike_id):
    """Create and return a new trail for a given user."""

    trail = Trail(user=user_id, hike=hike_id)

    db.session.add(trail)
    db.session.commit()

    return trail

def get_hikes():
    """Return all hiking trails."""

    return Hike.query.all()

def get_hikedetails_by_id(hike_id):
    """Return trail details for a selected trail"""

    return Hike.query.get(hike_id)

def get_user_by_email(email):
    """Return authenticated user details based on the email passed"""

    return User.query.filter(email == email).first()

if __name__ == "__main__":
    from server import app

    connect_to_db(server.app)
