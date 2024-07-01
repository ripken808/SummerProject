#!/usr/bin/python3

import cgi
import mysql.connector

print ("Content-type: text/html\n\n")

cnx = mysql.connector.connect(user='root', password='whipquan', host='mysql', database='security')
cursor = cnx.cursor()
form = cgi.FieldStorage()
username = form.getvalue('Username')
password = form.getvalue('Password')
found = False

if username and password:
    query = ("Select token FROM info WHERE username = %s AND password = %s")
    cursor.execute(query,(username, password))
    data = cursor.fetchone()
    if data:
        found = True
        token = data[0]
        print("<script>")
        print("document.cookie = 'username={}; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=\';".format(username))
        print("document.cookie = 'token={}; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=\';".format(token))
        print("window.location.href = 'home.py';")
        print("</script>")

print("<html>")

print("<title>Log in</title>")

print("<head>")
print("<style type=\"text/css\">")

print("label{")
print("width:100px;")
print("display:inline-block;")
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

print("#home{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("}")

print("#signup{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("right: 10px;") 
print("}")

print("#submit{")
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

print("<a href=\"signup.py\">")
print("<button id = \"signup\">Create an account</button>")
print("</a>")

print("<div id = \"form\">")
print("<form>")
print("<h2>Log in</h2>")
print("<label for=\"Username\">Username:</label>")
print("<input type=\"text\" id=\"Username\" name=\"Username\">")
print("<label for=\"Password\">Password:</label>")
print("<input type=\"password\" id=\"Password\" name=\"Password\"><br>")
print("<input type=\"submit\" name=\"submit\" id=\"submit\">")
if username and password and found == False:
    print("<p style=\"text-align : center\">Incorrect username or password :(<p>")
if (username and not password) or (password and not username):
    print("<p style=\"text-align : center\"> Please input a username and password <p>")
print("<form>")
print("</div>")

print("</body>")
print("</html>")

cursor.close()
cnx.close()