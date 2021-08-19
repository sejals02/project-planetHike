<h2> 🐾 Planet Hike </h2>

<p> Planet Hike is a full-stack web application which allows the users to search for the hiking places across the US National Parks, and around user's zipcodes.
It also allows to search the hiking trails based on the feature of interests such as dog friendly, kid friendly trails, difficulty levels to name a few search fitlers.
The idea of this website is to help users in their hiking journey.
</p>

<h2> Contents </h2>
<ul>
  <li> 
    <a href="#features"> Features </a>
  </li>
  <li>  
    <a href="#techstack"> Technology Stack </a>
   </li>
  <li> 
    <a href ="setup"> Set-up & Installation </a>
  </li>
  <li> 
    <a href ="about"> About the Developer </a> 
  </li>
  
<h2>
  <a id="user-content---features" class="anchor" area-hidden = "true" href ="##--features"></a>
    <a name = "user-content-features"></a>
     Features
</h2>      
<p> <b> Hompage </b>
 <ul>
    <li> Search all the national parks acorss the country</li>
    <li> User friendly search fitlers to search for the national park - Search by State, Search by National park name, Search by difficulty level, Search by features, Search near user zipcode</li>
    <li> Menu option with the sign in option<li>
  </ul>  
    
 <p> <b> Menu </b>
  <p> Authenticated session 
    <ul>
      <li> Profile </li>
      <li> Sign out </li>
      <li> Homepage </li>
    </ul>  
    <br>
  <p> UnAuthenticated session 
    <ul>
      <li> Profile </li>
      <li> Sign out </li>
      <li> Homepage </li>
    </ul>    
  <br>  
 <p> <b> Landing page with the list of hiking trails </b>
 <br>
 <p> <b> Landing page with the details of the hiking trails </b>
    <ul>
        <li> Trail details</li>
        <li> Weather</li>
        <li> Google map with customized pin </li>
        <li> Customization to favorite the trail </li>
      </ul>  
 <br>     
  <p> <b> Profile landing page </b>
    <ul>
        <li> List of the Favorited trails </li>
      </ul> 
  <br>
  <p> <b> Login page </b>
    <ul>
        <li> Sign in </li>
        <li> Create account </li>
        <li> Sign out </li>
      </ul>     

<h2>
  <a id="user-content---techstack" class="anchor" area-hidden = "true" href ="##--techstack"></a>
    <a name = "user-content-techstack"></a>
     Technology Stack
</h2> 

Language - <br>
CSS <br>
HTML <br>
Python <br>
Javascript <br>
Bootstrap <br>
FLASK<br>

Backend systems - <br>
PostreSQL <br>
SQLAlchemy <br>

APIs - <br>
Hikes api - https://www.kaggle.com/planejane/national-park-trails/metadata <br>
Weather api - https://pyowm.readthedocs.io <br>
Google maps <br>
Google places <br>


<h2>
  <a id="user-content---setup" class="anchor" area-hidden = "true" href ="##--setup"></a>
    <a name = "user-content-setup"></a>
     Setup and Installation
</h2> 

Install a code editor such as VS code or Sublime Text <br>
Install Python3 <br>
Install pip, the package installer for Python <br>
Install postgreSQL for the relational database <br>

Clone or fork repository: <br>
https://github.com/sejals02/project-planetHike <br>

Create and activate a virtual environment inside the planethike directory:<br>

$ virtualenv env<br>
$ source env/bin/activate<br>
Install dependencies:<br>

$ pip3 install -r requirements.txt<br>
<p>
Make an account with Google maps & get an API key.<br>
Make an account with PYOWM & get an API key.<br>

Store these keys in a file named 'secrets.sh'<br>
<p>
$ source secrets.sh <br>
<p>
With PostgreSQL, create the hikeplanet database <br>

$ createdb hikeplanet <br>
Create all tables and relations in the database and seed all data:<br>

$ python3 seed.py<br>
Run the app from the command line:<br>

$ python3 server.py<br>


<h2>
  <a id="user-content---about" class="anchor" area-hidden = "true" href ="##--about"></a>
    <a name = "user-content-about"></a>
     About the Developer
</h2> 

<p>Sejal is a Quality leader with 20+ years of experience in building and leading teams. While building and mentoring teams, she continued to learn new programming languages. Her passion for learning and growing her knowledge base is at the core of her belief, so she decided to add to those skills by enrolling in the engineering bootcamp at Hackbright as a full stack developer. She looks forward to building her skills and embarking her journey as a full-stack engineer post Hackbright. This is her first full-stack project. She can be found on <a href ="https://www.linkedin.com/in/sejalbiren/">LinkedIn </a> and on <a href="https://github.com/sejals02"> Github</a>.
