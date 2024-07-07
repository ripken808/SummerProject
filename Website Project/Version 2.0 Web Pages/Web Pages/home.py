#!/usr/bin/python3
#!- - - - - - - - - -!#

#TODO Import libraries needed for project
# ? Imports http.cookies to grab the session cookies.
import http.cookies
# ? Imports mysql.connector which allows me to connect to my database.
import mysql.connector
# ? Imports os to read the session cookies.
import os
# ? Imports cgi which allows me to grab the users input.
import cgi
#!- - - - - - - - - -!#

#TODO Makes sure that the python code can be executed as an html file
# ? Allows my python code to execute as an html file.
print ("Content-type: text/html\n\n")
#!- - - - - - - - - -!#

#TODO Create variables to be used thrughout the code
# ? Boolean to check if the user has a selected team
selected_team = None
# ? Sets up varaibles to store user inputs
form = cgi.FieldStorage()
username = None
token = None
found = False
# ? Connects me to my database
cnx = mysql.connector.connect(user='root', password='whipquan', host='mysql', database='security')
cursor = cnx.cursor()
# ? Grabs the cookies from the browser and stores them properly in the right variables.
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
#!- - - - - - - - - -!#

#TODO Checks to see if there is a current session and find query for the selected team
# ? Checks if there is a username and token cookie value stored in the browser.
if 'username' in cookie and 'token' in cookie:
    username = cookie['username'].value
    token = cookie['token'].value

#print(username)
#print(token)
# ? Checks if there is a username and token available.
if username and token:
# ? Queries the database to see if the username and token match and then it grabs the name of the selected team if it does.
    query = ("Select team FROM info WHERE username = %s AND token = %s")
    cursor.execute(query,(username, token))
    info = cursor.fetchone()
# ? If the username and token are found then it will save the selected team and change found to true.
    if info:
        selected_team = info[0]
        found = True
#print(selected_team)
#!- - - - - - - - - -!#

#TODO Checks to see if drop down menu is used and if the user already has a selected team 
# ? Checks to see if team is chosen in the drop down menu.
if 'selected-team' in form:
# ? Saves the value of the selected to the current user inside the database.
    selected_team = form.getvalue('selected-team')
    add_team = ("UPDATE info SET team = %s WHERE username = %s")
    cursor.execute(add_team, (selected_team, username))
    cnx.commit()
# ? Checks to see if a selected team already exists.
if selected_team is not None:
# ? Queries the database for the path of the teams image.
    query = "SELECT Path, abbreviation FROM teams WHERE team = '" + selected_team + "'"
    cursor.execute(query)
    data = cursor.fetchone()
# ? Saves the path and abbreviation of the team to variables.
    path = data[0]
    abr = data[1]
# ? Adds the abbreviation to the end of the default url to link to the baseball teams espn home page.
    print("<a href=\"https://www.espn.com/mlb/team/_/name/{}\" target=\"_blank\">".format(abr))
# ? Uses the path of the selected teams image to grab the image.
    print("<img src=\"{}\" alt=\"{}\" id=\"pic\">".format(path, selected_team)) 
    print("</a>")
#!- - - - - - - - - -!#

#TODO Use Html code to display content
# ? Sets the title of the page to Home.
print("<title>Home</title>")

print("<head>")

print("<style>")
# ? Sets the body of the page to have no borders.
print("body {")
print("margin: 0;")
print("padding: 0;")
print("}")
# ? Sets the size of the pictures and the location of them.
print("#pic{")
print("width: 300px;")
print("heght: auto;")
print("position: absolute;")
print("left: 50%;")
print("top: 0;")
print("transform: translateX(-50%);")
print("}")
# ? Sets the sign up button to the top right of the screen.
print("#signup{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("right: 10px;")      
print("}")
# ? Sets the log in button the top right of the screen next to the sign up button.
print("#login{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("right: 75px;")      
print("}")
# ? Sets the user button to the top right of the screen.
print("#user{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("right: 10px;")
print("}")
# ? Sets the h1 text to the center of the screen and adjusts the size and font.
print("h1{")
print("position: absolute;")
print("top: 50%;")
print("left: 50%;")
print("transform: translate(-50%,-50%);")
print("font-family: Verdana, Geneva, Tahoma, sans-serif;")
print("font-size: 50px;")
print("}")
# ? Adjusts the color, size and padding for the drop down button in the top left of the screen.
print(".dropbtn {")
print("background-color: #04AA6D;")
print("color: white;")
print("padding: 16px;")
print("font-size: 16px;")
print("border: none;")
print("}")
# ? Sets the style of the drop down.
print(".dropdown {")
print("position: relative;")
print("display: inline-block;")
print("}")
# ? Sets the style of the buttons inside of the drop down menu.
print(".dropdown-content {")
print("display: none;")
print("position: absolute;")
print("background-color: #f1f1f1;")
print("min-width: 160px;")
print("box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);")
print("z-index: 1;")
print("height: 50px;")
print("overflow: auto;")
print("}")
# ? Sets the style of each individual button inside the drop down menu.
print(".dropdown-content a {")
print("color: black;")
print("padding: 12px 16px;")
print("text-decoration: none;")
print("display: block;")
print("}")
# ? Sets a background color to the drop down content when it is being hovered.
print(".dropdown-content a:hover {background-color: #ddd;}")
# ? Sets the shape of the drop down content when the button is hovered.
print(".dropdown:hover .dropdown-content {display: block;}")
# ? Sets the background color of the drop down menu when being hovered.
print(".dropdown:hover .dropbtn {background-color: #3e8e41;}")
# ? Sets the size and position of the scrolling image section.
print("#images {")
print("top:100%;")
print("overflow: hidden;")
print("height: 200px;")
print("position: relative;")
print("}")
# ? Sets the position of the images inside the scrolling images and how fast they scroll.
print(".scroll-images {")
print("position: absolute;")
print("top:0px;")
print("left:0;")
print("overflow: hidden;")
print("white-space: nowrap;")
print("animation: scroll 30s linear infinite;")
print("width: auto;")
print("}")
# ? Sets the height of the images inside the scrolling image section.
print(".scroll-images img {")
print("width: 200px;")
print("height: auto;")
print("}")
# ? Sets how the images scroll from right to left in the auto scrolling section.
print("@keyframes scroll {")
print("0% { tansform: translateX(100%); }")
print("100% { transform: translateX(-50%); }")
print("}")
# ? When the scrolling image section is being hovered, the scrolling will stop.
print("#images:hover .scroll-images {")
print("animation-play-state:paused;")
print("}")


print("</style>")

print("</head>")
# ? Sets the background body color to dark purple.
print("<body bgcolor=\"#1a0d54\">")
# ? Creates a header in the middle of the screen. (Default message)
print("<h1 style=\"color: white\">Welcome to my server</h1>")
# ? Checks if there is a current session.
if found == True:
# ? Creates a user button with the user's name that links to the user's page.
    print("<a href=\"user.py\">")
    print("<button id=\"user\">" + username + "</button>")
    print("</a>")
#!- - - - - - - - - -!#

#TODO Create a drop down menu with a lsit of every mlb team
    print("<div class=\"dropdown\">")
    print("<button class=\"dropbtn\">Baseball Teams</button>")
    print("<div class=\"dropdown-content\">")
    print("<form id=\"teamForm\" method=\"post\" action=\"\">") 
    # ? If any button is selected it will save the teams name to the selected team variable.
    print("<button name=\"selected-team\" type=\"submit\" value=\"Arizona Diamondbacks\">Arizona Diamondbacks</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Atlanta Braves\">Atlanta Braves</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Baltimore Orioles\">Baltimore Orioles</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Boston Red Sox\">Boston Red Sox</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Chicago Cubs\">Chicago Cubs</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Chicago White Sox\">Chicago White Sox</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Cincinnati Reds\">Cincinnati Reds</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Cleveland Guardians\">Cleveland Guardians</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Colorado Rockies\">Colorado Rockies</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Detroit Tigers\">Detroit Tigers</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Houston Astros\" >Houston Astros</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Kansas City Royals\">Kansas City Royals</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Los Angeles Angels\">Los Angeles Angels</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Los Angeles Dodgers\">Los Angeles Dodgers</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Miami Marlins\">Miami Marlins</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Milwaukee Brewers\">Milwaukee Brewers</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Minnesota Twins\">Minnesota Twins</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"New York Mets\">New York Mets</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"New York Yankees\">New York Yankees</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Oakland Athletics\">Oakland Athletics</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Philadelphia Phillies\">Philadelphia Phillies</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Pittsburgh Pirates\">Pittsburgh Pirates</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"San Diego Padres\">San Diego Padres</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"San Francisco Giants\">San Francisco Giants</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Seattle Mariners\">Seattle Mariners</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"St. Louis Cardinals\">St. Louis Cardinals</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Tampa Bay Rays\">Tampa Bay Rays</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Texas Rangers\">Texas Rangers</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Toronto Blue Jays\">Toronto Blue Jays</button>")
    print("<button name=\"selected-team\" type=\"submit\" value=\"Washington Nationals\">Washington Nationals</button>")
    print("</form>")
    print("</div>")
    print("</div>")
#!- - - - - - - - - -!#

#TODO Auto scrolling section
# ? Creates an auto scrolling section that shows a picture of every mlb team.
    print("<div id=\"images\">")
    print("<div class=\"scroll-images\">")
# ? Uses every team twice so it has seemless auto scrolling.
    print("<img src=\"teams/Diamondbacks.png\">")
    print("<img src=\"teams/Braves.png\">")
    print("<img src=\"teams/Orioles.png\">")
    print("<img src=\"teams/Red-Sox.png\">")
    print("<img src=\"teams/Cubs.png\">")
    print("<img src=\"teams/White-Sox.png\">")
    print("<img src=\"teams/Reds.png\">")
    print("<img src=\"teams/Guardians.png\">")
    print("<img src=\"teams/Rockies.png\">")
    print("<img src=\"teams/Tigers.png\">")
    print("<img src=\"teams/Astros.png\">")
    print("<img src=\"teams/Royals.png\">")
    print("<img src=\"teams/Angels.png\">")
    print("<img src=\"teams/Dodgers.png\">")
    print("<img src=\"teams/Marlins.png\">")
    print("<img src=\"teams/Brewers.png\">")
    print("<img src=\"teams/Twins.png\">")
    print("<img src=\"teams/Mets.png\">")
    print("<img src=\"teams/Yankees.png\">")
    print("<img src=\"teams/Athletics.png\">")
    print("<img src=\"teams/Phillies.png\">")
    print("<img src=\"teams/Pirates.png\">")
    print("<img src=\"teams/Padres.png\">")
    print("<img src=\"teams/Giants.png\">")
    print("<img src=\"teams/Mariners.png\">")
    print("<img src=\"teams/Cardinals.png\">")
    print("<img src=\"teams/Rays.png\">")
    print("<img src=\"teams/Rangers.png\">")
    print("<img src=\"teams/Blue-Jays.png\">")
    print("<img src=\"teams/Nationals.png\">")
    print("<img src=\"teams/Diamondbacks.png\">")
    print("<img src=\"teams/Braves.png\">")
    print("<img src=\"teams/Orioles.png\">")
    print("<img src=\"teams/Red-Sox.png\">")
    print("<img src=\"teams/Cubs.png\">")
    print("<img src=\"teams/White-Sox.png\">")
    print("<img src=\"teams/Reds.png\">")
    print("<img src=\"teams/Guardians.png\">")
    print("<img src=\"teams/Rockies.png\">")
    print("<img src=\"teams/Tigers.png\">")
    print("<img src=\"teams/Astros.png\">")
    print("<img src=\"teams/Royals.png\">")
    print("<img src=\"teams/Angels.png\">")
    print("<img src=\"teams/Dodgers.png\">")
    print("<img src=\"teams/Marlins.png\">")
    print("<img src=\"teams/Brewers.png\">")
    print("<img src=\"teams/Twins.png\">")
    print("<img src=\"teams/Mets.png\">")
    print("<img src=\"teams/Yankees.png\">")
    print("<img src=\"teams/Athletics.png\">")
    print("<img src=\"teams/Phillies.png\">")
    print("<img src=\"teams/Pirates.png\">")
    print("<img src=\"teams/Padres.png\">")
    print("<img src=\"teams/Giants.png\">")
    print("<img src=\"teams/Mariners.png\">")
    print("<img src=\"teams/Cardinals.png\">")
    print("<img src=\"teams/Rays.png\">")
    print("<img src=\"teams/Rangers.png\">")
    print("<img src=\"teams/Blue-Jays.png\">")
    print("<img src=\"teams/Nationals.png\">")

    print("</div>")

    print("</div>")
#!- - - - - - - - - -!#

#TODO Create a default page if there is no current session
else:
# ? Creates a log in button that links to the log in page.
    print("<div id=\"buttons\">")
    print("<a href=\"login.py\">")
    print("<button id=\"login\">Log in</button>")
    print("</a>")
# ? Creates a sign up button that links to the sign up page.
    print("<a href=\"signup.py\">")
    print("<button id=\"signup\">Sign up</button>")
    print("</a>")
    print("</div>")

print("</body>")

print("</html>")
#!- - - - - - - - - -!#

#TODO Close opened files.
cursor.close()
cnx.close()