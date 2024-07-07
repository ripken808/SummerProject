#!/usr/bin/python3
#!- - - - - - - - - -!#

#TODO Import libraries needed for project
# ? Imports http.cookies to grab the session cookies.
import http.cookies
# ? Imports os to read the session cookies.
import os
#!- - - - - - - - - -!#

#TODO Makes sure that the python code can be executed as an html file
# ? Allows my python code to execute as an html file.
print ("Content-type: text/html\n\n")
#!- - - - - - - - - -!#

#TODO Create variables to be used thrughout the code
# ? Grabs the cookies from the browser and stores them properly in the right variables.
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
username = cookie.get('username').value
token = cookie.get('token').value
#!- - - - - - - - - -!#

#TODO Use Html code to display content
print("<html>")

print("<head>")
# ? Sets the title of the page to the 'username' Info.
print("<title>" + username + " Info </title>")

# ? Creates a method to clear cookies from the browser and end the session.
print("<script>")

print("function signout() {")
print("document.cookie = 'username=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=\';")
print("document.cookie = 'token=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=\';")
print("document.cookie = 'team=; expires Thu, 01 Jan 1970 00:00:00 GMT; path=\';")
# ? Sends the user to the log out page.
print("window.location.href = 'logout.py';")
print("}")

print("</script>")

print("<style>")
# ? Sets the sign out button to the top right of the page.
print("#signout{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("right: 10px;")      
print("}")
# ? Sets the home button to the top left of the screen.
print("#home{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("}")

print("</style>")
print("</head>")
# ? Sets the body background color to dark purple.
print("<body bgcolor=\"#1a0d54\">")
# ? Creates a home button that links to the home page.
print("<a href=\"home.py\">")
print("<button id=\"home\">Home</button>")
print("</a>")
# ? Creates a sign out button that will call on the signout function once clicked.
print("<button id=\"signout\" onclick=\"signout()\">Sign Out</button>")

print("</body>")

print("</html>")
