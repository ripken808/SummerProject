#!/usr/bin/python3

import http.cookies
import mysql.connector
import os

print ("Content-type: text/html\n\n")

cnx = mysql.connector.connect(user='root', password='whipquan', host='mysql', database='security')
cursor = cnx.cursor()

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))

username = None
token = None
found = False

if 'username' in cookie and 'token' in cookie:
    username = cookie['username'].value
    token = cookie['token'].value

if username and token:
    query = ("Select username FROM info WHERE username = %s AND token = %s")
    cursor.execute(query,(username, token))
    if cursor.fetchone():
        found = True

print("<title>Home</title>")

print("<head>")

print("<style>")

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

print("</style>")

print("</head>")

print("<body bgcolor=\"#1a0d54\">")

print("<h1 style=\"color: white\">Welcome to my server</h1>")

if found == True:
    print("<a href=\"user.py\">")
    print("<button id=\"user\">" + username + "</button>")
    print("</a>")

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