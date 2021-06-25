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

    return render_template("all_hikes.html", hikes=hikes)

@app.route("/hikes/<hike_id>")
def show_hikedetails(hike_id):
    """Show details on a particular hiking trail."""

    hikedetails = crud.get_hikedetails_by_id(hike_id)
    features = hikedetails.features.split(",")
    print(features)
    print(type(features))

    return render_template("hike_details.html", hikedetails=hikedetails)

@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    
    if not user or user.password != password:
        flash ("The email or password you entered was incorrect.")
    else:
    #     # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.fname} !")

    return redirect("/")    

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

