#!/usr/bin/python3

import http.cookies
import mysql.connector
import os
import cgi

print ("Content-type: text/html\n\n")

selected_team = None
form = cgi.FieldStorage()
cnx = mysql.connector.connect(user='root', password='whipquan', host='mysql', database='security')
cursor = cnx.cursor()
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
username = None
token = None
found = False

if 'username' in cookie and 'token' in cookie:
    username = cookie['username'].value
    token = cookie['token'].value

#print(username)
#print(token)
if username and token:
    query = ("Select team FROM info WHERE username = %s AND token = %s")
    cursor.execute(query,(username, token))
    info = cursor.fetchone()
    if info:
        selected_team = info[0]
        found = True
#print(selected_team)
if 'selected-team' in form:
    selected_team = form.getvalue('selected-team')
    add_team = ("UPDATE info SET team = %s WHERE username = %s")
    cursor.execute(add_team, (selected_team, username))
    cnx.commit()
if selected_team is not None:
    query = "SELECT Path, abbreviation FROM teams WHERE team = '" + selected_team + "'"
    cursor.execute(query)
    data = cursor.fetchone()
    path = data[0]
    abr = data[1]
    print("<a href=\"https://www.espn.com/mlb/team/_/name/{}\" target=\"_blank\">".format(abr))
    print("<img src=\"{}\" alt=\"{}\" id=\"pic\">".format(path, selected_team)) 
    print("</a>")

print("<title>Home</title>")

print("<head>")

print("<style>")

print("#pic{")
print("width: 300px;")
print("heght: auto;")
print("position: absolute;")
print("left: 50%;")
print("top: 0;")
print("transform: translateX(-50%);")
print("}")

print("#signup{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("right: 10px;")      
print("}")

print("#login{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("right: 75px;")      
print("}")

print("#user{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("right: 10px;")
print("}")

print("h1{")
print("position: absolute;")
print("top: 50%;")
print("left: 50%;")
print("transform: translate(-50%,-50%);")
print("font-family: Verdana, Geneva, Tahoma, sans-serif;")
print("font-size: 50px;")
print("}")

print(".dropbtn {")
print("background-color: #04AA6D;")
print("color: white;")
print("padding: 16px;")
print("font-size: 16px;")
print("border: none;")
print("}")

print(".dropdown {")
print("position: relative;")
print("display: inline-block;")
print("}")

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

print(".dropdown-content a {")
print("color: black;")
print("padding: 12px 16px;")
print("text-decoration: none;")
print("display: block;")
print("}")

print(".dropdown-content a:hover {background-color: #ddd;}")

print(".dropdown:hover .dropdown-content {display: block;}")

print(".dropdown:hover .dropbtn {background-color: #3e8e41;}")

print("</style>")

print("</head>")

print("<body bgcolor=\"#1a0d54\">")

print("<h1 style=\"color: white\">Welcome to my server</h1>")

if found == True:
    print("<a href=\"user.py\">")
    print("<button id=\"user\">" + username + "</button>")
    print("</a>")
    
    print("<div class=\"dropdown\">")
    print("<button class=\"dropbtn\">Baseball Teams</button>")
    print("<div class=\"dropdown-content\">")
    print("<form id=\"teamForm\" method=\"post\" action=\"\">") 
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
else:
    print("<div id=\"buttons\">")
    print("<a href=\"login.py\">")
    print("<button id=\"login\">Log in</button>")
    print("</a>")

    print("<a href=\"signup.py\">")
    print("<button id=\"signup\">Sign up</button>")
    print("</a>")
    print("</div>")

print("</body>")

print("</html>")

cursor.close()
cnx.close()