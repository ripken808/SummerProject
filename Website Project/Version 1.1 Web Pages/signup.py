#!/usr/bin/python3

import cgi
import mysql.connector
import secrets

print ("Content-type: text/html\n\n")

def generate_token():
    return secrets.token_hex(16)

cnx = mysql.connector.connect(user='root', password='whipquan', host='mysql', database='security')
cursor = cnx.cursor()

form = cgi.FieldStorage()
username = form.getvalue('Username')
password = form.getvalue('Password')
confirm = form.getvalue('Confirm')

submit_clicked = 'submit' in form

print("<title>Sign up</title>")

print("<html>")

print("<head>")

print("<style>")

print("#home{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("}")

print("#login{")
print("border-radius: 10px;")
print("position: absolute;")
print("top: 0;")
print("right: 10px;") 
print("}")

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

print("label{")
print("width:100px;")
print("display:inline-block;")
print("}")

print("#submit, #login{")
print("width: 250px;")
print("margin-top: 10px;")
print("}")

print("h2{")
print("text-align: center;")
print("}")

print("</style>")

print("</head>")

print("<body bgcolor=\"#1a0d54\">")

print("<a href=\"home.py\">")
print("<button id=\"home\">Home</button>")
print("</a>")

print("<a href=\"login.py\">")
print("<button id = \"login\">Already have an account?</button>")
print("</a>")

print("<div id = \"form\">")

print("<form>")

print("<h2>Sign up</h2>")

print("<label for=\"Username\">Username:</label>")
print("<input type=\"text\" id=\"Username\" name=\"Username\">")
print("<label for=\"Password\">Password:</label>")
print("<input type=\"password\" id=\"Password\" name=\"Password\"><br>")
print("<label for=\"Confirm\">Confirm Password:</label>")
print("<input type=\"password\" id=\"Confirm\" name=\"Confirm\"><br>")
print("<input type=\"submit\" name=\"submit\" id=\"submit\">")

if (username and password) and (password == confirm):
    query = ("Select username FROM info WHERE username = '" + username + "'")
    cursor.execute(query)
    if cursor.fetchone():
        print("<p style=\"text-align: center\">Username {} is already in use :(</p>".format(username))
    
    else:
        token = generate_token()
        add_user = ("INSERT INTO info (username, password, token) VALUE (%s, %s, %s)")
        cursor.execute(add_user,(username, password, token))
        print("<script>")
        print("document.cookie = 'username={}; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=\';".format(username))
        print("document.cookie = 'token={}; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=\';".format(token))
        print("window.location.href = 'home.py';")
        print("</script>")

if submit_clicked and (not username or not password or not confirm):
    print("<p style=\"text-align : left\"> You are missing: <br>")
    if not username: 
        print("- Username<br>")
    if not password:
        print("- Password<br>")
    if not confirm:
        print("- Confirmation fo password<br>")
    print("</p>")

elif password != confirm:
    print("<p style=\"text-align : center\"> Your password does not match <p>")
 
print("</div>")

print("</body>")

print("</html>")

cnx.commit()
cursor.close()
cnx.close()