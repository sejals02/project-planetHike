"""CRUD operations."""

from model import db, User, Hike, Trail, connect_to_db
import server
from sqlalchemy import distinct


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

def get_hikedetails_by_state(state):
    """Return hiking places for a searched state"""

    state_hikes = Hike.query.filter(Hike.state_name == state).all()
    return state_hikes

def get_hikedetails_by_np(nationalpark):
    """Return hiking places for a searched national park"""

    np_hikes = Hike.query.filter(Hike.area_name.like(nationalpark + '%')).all()
    return np_hikes

def get_nationalpark_name(nationalpark):
    """Return full national park name if user searched with a partial national park name"""

    np_name = Hike.query.filter(Hike.area_name.like(nationalpark + '%')).first()
    return np_name

def get_hikedetails_by_difficultylevel(dl):
    """Return list of hike trails per the difficuly level"""

    if (dl == "Easy"):
       nationalpark = Hike.query.filter((Hike.difficulty_level == '1') | (Hike.difficulty_level == '2')).all()

    elif (dl == "Moderate"):
        nationalpark = Hike.query.filter((Hike.difficulty_level == '3') | (Hike.difficulty_level == '4')).all()

    elif (dl == "Hard"):
        nationalpark = Hike.query.filter(Hike.difficulty_level > '4').all()
    
    return nationalpark

def get_hikedetails_by_feature(feature):
    """ Return the list of hikes per feature """

    if (feature == "dog"):
       npbyfeature = Hike.query.filter(Hike.features.like('%dogs-leash%')).all()

    if (feature == "kid"):
       npbyfeature = Hike.query.filter(Hike.features.like('%kids%') | Hike.features.like('%strollers%')).all()
  
    if (feature == "water"):
       npbyfeature = Hike.query.filter(Hike.features.like('%river%') | Hike.features.like('%beach%')).all()

    
    return npbyfeature

def get_hikedetails_by_userloc(k):
    """ Retrun the list of the trails within 50 miles radius of the entered zipcode"""
    
    npbyuserloc = Hike.query.filter(Hike.area_name == k).all()

    return npbyuserloc

def create_user(email, password, fname, lname):
    """Create and return a new user."""

    user = User(email=email, password=password, fname=fname, lname=lname)

    db.session.add(user)
    db.session.commit()

    return user
    
def get_user_by_email(email):
    """Return authenticated user details based on the email passed"""

    user = User.query.filter(User.email == email).first()
    # print (f"from crud {u}")
    return user

def save_favorited_trail(hike_id, user_id):
    """ Write to Trails table with the user's favorited hike. """

    trail = Trail(hike_id = hike_id, user_id = user_id)

    db.session.add(trail)
    db.session.commit()

    return (trail)

if __name__ == "__main__":
    from server import app

    connect_to_db(server.app)
