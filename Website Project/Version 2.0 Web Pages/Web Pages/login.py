#!/usr/bin/python3
#!- - - - - - - - - -!#

#TODO Import libraries needed for project
# ? Imports cgi which allows me to grab the users input.
import cgi
# ? Imports mysql.connector which allows me to connect to my database.
import mysql.connector
#!- - - - - - - - - -!#

#TODO Makes sure that the python code can be executed as an html file
# ? Allows my python code to execute as an html file.
print ("Content-type: text/html\n\n")
#!- - - - - - - - - -!#

#TODO Create variables to be used thrughout the code
# ? Connects me to my database
cnx = mysql.connector.connect(user='root', password='whipquan', host='mysql', database='security')
cursor = cnx.cursor()
# ? Sets up varaibles to store user inputs
form = cgi.FieldStorage()
username = form.getvalue('Username')
password = form.getvalue('Password')
# ? Variable to check if user input is found inside of database
found = False
#!- - - - - - - - - -!#

#TODO Query the database and create cookies for session
# ? Checks if the form is fully filled out.
if username and password:
# ? Queries my database with the user input.
    query = ("Select token FROM info WHERE username = %s AND password = %s")
    cursor.execute(query,(username, password))
    data = cursor.fetchone()
# ? If found, create cookies for session.
    if data:
        found = True
        token = data[0]
        print("<script>")
# ? Creates cookies for the session that includs username and token.
        print("document.cookie = 'username={}; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=\';".format(username))
        print("document.cookie = 'token={}; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=\';".format(token))
        print("window.location.href = 'home.py';")
        print("</script>")
#!- - - - - - - - - -!#

#TODO Use Html code to display content
print("<html>")
# ? Sets title to Log in
print("<title>Log in</title>")

print("<head>")
print("<style type=\"text/css\">")
# ? Sets size of labels next to user input.
print("label{")
print("width:100px;")
print("display:inline-block;")
print("}")
# ? Sets my log in form to the center of the page and customizes the color and size.
print("#form{")
print("border-radius: 10px;")
print("background:black;")
print("color:white;")
print("width:251px;")
print("padding:4px;")
print("position: absolute;")
print("top: 50%;")
print("left: 50%;")
print("transform: translate(-50%,-50%);")
print("}")
# ? Sets the home button to the top left.
print("#home{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("}")
# ? Sets the sign up button to the top right.
print("#signup{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("right: 10px;") 
print("}")
# ? Sets the size of the submit button.
print("#submit{")
print("width: 250px;")
print("margin-top: 10px;")
print("}")
# ? Centers my h2 text.
print("h2{")
print("text-align: center;")
print("}")

print("</style>")

print("</head>")
# ? Sets the body background color to dark purple.
print("<body bgcolor=\"#1a0d54\">")
# ? Creates a home button that links to the home page.
print("<a href=\"home.py\">")
print("<button id=\"home\">Home</button>")
print("</a>")
# ? Creates a sign up button that links to the sign up button.
print("<a href=\"signup.py\">")
print("<button id = \"signup\">Create an account</button>")
print("</a>")
# ? Creates the section for where the user input will be.
print("<div id = \"form\">")
print("<form>")
print("<h2>Log in</h2>")
# ? Creates all of the labels and user input boxes.
print("<label for=\"Username\">Username:</label>")
print("<input type=\"text\" id=\"Username\" name=\"Username\">")
print("<label for=\"Password\">Password:</label>")
print("<input type=\"password\" id=\"Password\" name=\"Password\"><br>")
print("<input type=\"submit\" name=\"submit\" id=\"submit\">")
#!- - - - - - - - - -!#

#TODO Checks to make sure that user is properly using log in form and gives feedback
# ? Checks if the user information given is inside of the database.
if username and password and found == False:
    print("<p style=\"text-align : center\">Incorrect username or password :(<p>")
# ? Checks if the user fully filled out the form.
if (username and not password) or (password and not username):
    print("<p style=\"text-align : center\"> Please input a username and password <p>")
print("<form>")
print("</div>")

print("</body>")
print("</html>")
#!- - - - - - - - - -!#

#TODO Close opened files.
cursor.close()
cnx.close()