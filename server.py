"""Server for Planet Hike app."""

from flask import *
# from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import requests
import googlemaps
import pandas as pd
import pyowm

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
    cityname = (hikedetails.city_name)

    """Provide weather for a national park"""
    #pyowm API key
    pyown_APIKEY = '305bdfa862b07afb5ea55af3f568513d'
    # Use API key to get data
    OpenWMap=pyowm.OWM(pyown_APIKEY)
    # give where you need to see the weather  
    try:
        Weather=OpenWMap.weather_at_place(cityname)  
        # get out data in the mentioned location
        Data=Weather.get_weather() 
        # get current temparature in Farenheit 
        temp = Data.get_temperature(unit='fahrenheit')  
        curr_temp = temp['temp']  
        min_temp = temp['temp_min']
        max_temp = temp['temp_max']

        if curr_temp:
            return render_template("hike_details.html", hikedetails=hikedetails, curr_temp=curr_temp, min_temp=min_temp, max_temp=max_temp)
    except:
         return render_template("hike_details.html", hikedetails=hikedetails,curr_temp=None, min_temp=None, max_temp=None)   

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

@app.route("/searchbyuserloc", methods=["POST"])
def show_resultsby_userloc():
    """Show result for national park within 50 miles radious of user location."""
    
    zcode = request.form.get("userloc")

    #google api key
    API_KEY = 'AIzaSyDcOp-SCFmsmDFlZfjKPU45YUYon80LrhQ'

    params = {
        'key' : API_KEY,
        'address': zcode
    }
    #Based on the user entered zipcode, processing and getting lat/lon 
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url, params=params).json()
    response.keys()

    if response['status'] == 'OK':
        geometry = response['results'][0]['geometry']
        lat = geometry['location']['lat']
        lon = geometry['location']['lng']

    #using google places api to get the park list from within 50 mile radious of user input zipcode
    map_client = googlemaps.Client(API_KEY)

    location = (lat, lon)
    search_string = "National Park"
    distance = 50 * 1609.344
    park_list = []
    hikes = []

    response = map_client.places_nearby(
        location = location,
        keyword = search_string,
        radius = distance #in meters
    )

    i = 0
    for p in response:
        park_list.append(response['results'][i]['name'])
        i += 1

    for k in park_list:
        hikes.extend(crud.get_hikedetails_by_userloc(k))
        
    if len(hikes) > 0:
            return render_template("all_hikes.html",zcode=zcode,hikes = hikes, nationalpark=None,state=None, dl=None, feature=None)      
    else:
            flash(f"No results found for the zipcode {zcode}. Please try again")
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

