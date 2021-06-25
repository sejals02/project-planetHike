"""Project planethike

Script to seed database.
"""

import os
import csv
from faker import Faker
#from random import choice, randint

import model
import crud
import server

os.system("dropdb hikeplanet")
os.system("createdb hikeplanet")

model.connect_to_db(server.app)
model.db.create_all()

# Load hiking places data from csv file
with open('data/original_nationalpark_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

# print the list of entire hiking places file 
    # for row in reader:
    #    print(row['name'], row['area_name'])

# Create and store the hiking place from csv to database
    for row in reader:
   
        name = row["name"]
        area_name = row["area_name"]
        city_name = row["city_name"]
        state_name = row["state_name"]
        country_name = row["country_name"]
        geoloc = row["_geoloc"]
        difficulty_level = row["difficulty_rating"]
        #Convert meters to miles 
        miles = float(row["length"])/1609.344
        # print(miles)
        # print(type(miles))
        # print('**************')
        features = str(row["features"])
        avg_rating = row["avg_rating"]
        
        db_hike = crud.create_hike(name, area_name, city_name, state_name, country_name, geoloc, difficulty_level, miles, features, avg_rating)
    
# Load users from faker
fake = Faker()
for n in range(10):
    fname = fake.first_name()
    lname = fake.last_name()
    #email = fake.email()
    email = fname + "." + lname + "@gmail.com"
    #password = fake.password(length = 5)
    password = "12345"

    crud.create_user(fname, lname, email, password)

