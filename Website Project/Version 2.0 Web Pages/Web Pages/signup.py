#!/usr/bin/python3
#!- - - - - - - - - -!#

#TODO Import libraries needed for project
# ? Imports cgi which allows me to grab the users input.
import cgi
# ? Imports mysql.connector which allows me to connect to my database.
import mysql.connector
# ? Imports secrets which allows me to create a unique 32 character token for new users.
import secrets
#!- - - - - - - - - -!#

#TODO Makes sure that the python code can be executed as an html file
# ? Allows my python code to execute as an html file.
print ("Content-type: text/html\n\n")
#!- - - - - - - - - -!#

#TODO Create methods and variables to be used thrughout the code
# ? A method that when called upon cretes a 32 character unique token for a user.
def generate_token():
    return secrets.token_hex(16)

# ? Connects me to my database
cnx = mysql.connector.connect(user='root', password='whipquan', host='mysql', database='security')
cursor = cnx.cursor()
# ? Sets up varaibles to store user inputs
form = cgi.FieldStorage()
username = form.getvalue('Username')
password = form.getvalue('Password')
confirm = form.getvalue('Confirm')
submit_clicked = 'submit' in form
#!- - - - - - - - - -!#

#TODO Use Html code to display content
# ? Sets the title of the page
print("<title>Sign up</title>")

print("<html>")

print("<head>")

print("<style>")
# ? Sets the home button to the top left of the page.
print("#home{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("}")
# ? Sets the log in button to the top right of the page.
print("#login{")
print("border-radius: 10px;")
print("position: absolute;")
print("top: 0;")
print("right: 10px;") 
print("}")
# ? Sets the sign up section to the middle of the screen.
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
# ? Sets the size of the labels next to the input boxes.
print("label{")
print("width:100px;")
print("display:inline-block;")
print("}")
# ? Sets the size of the log in and submit button.
print("#submit, #login{")
print("width: 250px;")
print("margin-top: 10px;")
print("}")
# ? Centers the h2 text.
print("h2{")
print("text-align: center;")
print("}")

print("</style>")

print("</head>")
# ? Sets the background color of the body to dark purple.
print("<body bgcolor=\"#1a0d54\">")
# ? Creates a button that links to the home page.
print("<a href=\"home.py\">")
print("<button id=\"home\">Home</button>")
print("</a>")
# ? Creates a button that links to the log in page.
print("<a href=\"login.py\">")
print("<button id = \"login\">Already have an account?</button>")
print("</a>")
# ? Sets up a section on the page where the user will be inputing information to sign up.
print("<div id = \"form\">")
print("<form>")
print("<h2>Sign up</h2>")
# ? Creates the labels and inputs for the user to use to sign up.
print("<label for=\"Username\">Username:</label>")
print("<input type=\"text\" id=\"Username\" name=\"Username\">")
print("<label for=\"Password\">Password:</label>")
print("<input type=\"password\" id=\"Password\" name=\"Password\"><br>")
print("<label for=\"Confirm\">Confirm Password:</label>")
print("<input type=\"password\" id=\"Confirm\" name=\"Confirm\"><br>")
print("<input type=\"submit\" name=\"submit\" id=\"submit\">")
#!- - - - - - - - - -!#

#TODO give feedback to the user if they are not properly signing up
# ? Checks if the user has properly filled out all sections.
if (username and password) and (password == confirm):
# ? Queries the data base to check if the username already exists.
    query = ("Select username FROM info WHERE username = '" + username + "'")
    cursor.execute(query)
# ? If the username exits then it will let the user know that they cannot use this username.
    if cursor.fetchone():
        print("<p style=\"text-align: center\">Username {} is already in use :(</p>".format(username))
# ? If it the username does not exit then it will write to the data base the username, password, and token.
    else:
        token = generate_token()
        add_user = ("INSERT INTO info (username, password, token) VALUE (%s, %s, %s)")
        cursor.execute(add_user,(username, password, token))
        print("<script>")
# ? Stores the username and token to the browser as cookies.
        print("document.cookie = 'username={}; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=\';".format(username))
        print("document.cookie = 'token={}; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=\';".format(token))
# ? Once everything is stored inside the database, it will link the user home with the cookies stored inside the browser.
        print("window.location.href = 'home.py';")
        print("</script>")
# ? Checks if the user fully filled out the form.
if submit_clicked and (not username or not password or not confirm):
# ? Will let the user know what they are missing to input.
    print("<p style=\"text-align : left\"> You are missing: <br>")
    if not username: 
        print("- Username<br>")
    if not password:
        print("- Password<br>")
    if not confirm:
        print("- Confirmation fo password<br>")
    print("</p>")
# ? Checks if the users password matches the confirmation of the password.
elif password != confirm:
# ? If it does not match it will let the user know.
    print("<p style=\"text-align : center\"> Your password does not match <p>")

print("</div>")
print("</body>")

print("</html>")
#!- - - - - - - - - -!#

#TODO Close opened files.
cnx.commit()
cursor.close()
cnx.close()