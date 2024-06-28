#!/usr/bin/python3

import cgi

print ("Content-type: text/html\n\n")

form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

print("<html>")

print("<head>")

print("<title>" + username + " Info </title>")

print("<script>")

print("function home() {")
print("    var username = '{}';".format(username))
print("    var password = '{}';".format(password))
print("    window.location.href = 'home.py?username=' + encodeURIComponent(username) + '&password=' + encodeURIComponent(password);")
print("}")

print("</script>")

print("<style>")

print("#signout{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("right: 10px;")      
print("}")

print("#home{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("}")

print("</style>")

print("</head>")

print("<body bgcolor=\"#1a0d54\">")

print("<button id=\"home\" onclick=\"home()\">Home</button>")

print("<a href=\"home.py\">")
print("<button id=\"signout\">Sign Out</button>")
print("</a>")

print("</body>")

print("</html>")