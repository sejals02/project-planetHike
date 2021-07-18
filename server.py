"""Server for Planet Hike app."""

from flask import *
# from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

#Homepage!
@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")

@app.route("/hike")
def all_hikes():
    """View all hiking trails list."""

    hikes = crud.get_hikes()

    return render_template("all_hikes.html", hikes=hikes,  state=None, nationalpark=None, dl_hikes=None, dl=None, feature=None)

@app.route("/hikes/<hike_id>")
def show_hikedetails(hike_id):
    """Show details on a particular hiking trail."""

    hikedetails = crud.get_hikedetails_by_id(hike_id)
    features = (hikedetails.features)
    print(features)
    print(type(features))

    return render_template("hike_details.html", hikedetails=hikedetails)

@app.route("/searchbystate", methods=["POST"])
def show_hikedetails_byState():
    """Show details on a particular hiking trail."""

    state = request.form.get("state")
    hikes = crud.get_hikedetails_by_state(state)

    if hikes:
        return render_template("all_hikes.html", hikes=hikes, state=state, nationalpark=None, dl_hikes=None)       
        
    else:    
        flash("Please enter full name of the US state, eg. California. No State abbreviations are allowed")
        return redirect("/")

@app.route("/searchbydifficultylevel", methods=["POST"])
def show_hikedetails_bydiffcultylevel():
    """Show hikes based on the difficulty level."""

    dl = request.form.get("difficulty_level")

    hikes = crud.get_hikedetails_by_difficultylevel(dl)

    if hikes:
        return render_template("all_hikes.html", dl = dl, hikes=hikes, state=None, nationalpark=None)       
        
    else:    
        flash("Please select any of the search criteria prvided on the website for searching the hiking trails")
    return redirect("/") 

@app.route("/searchbyfeature", methods=["POST"])
def show_hikedetails_byfeature():
    """Show list of hikes based on the feature."""

    feature = request.form.get("feature")

    hikes = crud.get_hikedetails_by_feature(feature)

    if hikes:
        return render_template("all_hikes.html", feature=feature, hikes=hikes, dl=None, state=None, nationalpark=None)       
        
    else:    
        flash("Please select any of the search criteria provided on the website for searching the hiking trails")
    return redirect("/")            

@app.route("/searchbynp", methods=["POST"])
def show_hikedetails_byNationalpark():
    """Show list of all the hiking trails for a national park."""

    nationalpark = request.form.get("np")

    hikes = crud.get_hikedetails_by_np(nationalpark)

    npname = crud.get_nationalpark_name(nationalpark)

    if hikes:
        return render_template("all_hikes.html", hikes=hikes, nationalpark=nationalpark, npname = npname, state=None)       
        
    else:    
        flash("Please enter full name of a national park, eg. Yellowstone National Park.")
        return redirect("/")   

@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")

    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    print (user)
    
    if not user or user.password != password:
        flash ("The email or password you entered was incorrect. Please try again")
    else:
    #     # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back {user.fname}")

    return redirect("/")    

@app.route("/users", methods=["POST"])
def create_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")
    fname = request.form.get("fname")
    lname = request.form.get("lname")

    user = crud.get_user_by_email(email)

    if user:
        flash("User account already exists with that email.")
    else:    
        crud.create_user(email, password, fname, lname)
        flash("Account created successfully! Please log in.")
        
    return redirect("/")

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

