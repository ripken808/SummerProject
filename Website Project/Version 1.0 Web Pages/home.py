#!/usr/bin/python3

import cgi

print ("Content-type: text/html\n\n")

form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

print("<title>Home</title>")

print("<script>")
print("function user() {")
print("var username = '{}'".format(username))
print("var password = '{}'".format(password))
print("window.location.href = 'user.py?username=' + encodeURIComponent(username) + '&password=' + encodeURIComponent(password);")
print("}")
print("</script>")

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

if not username and not password:
    print("<div id=\"buttons\">")
    
    print("<a href=\"login.py\">")
    print("<button id=\"login\">Log in</button>")
    print("</a>")

    print("<a href=\"signup.py\">")
    print("<button id=\"signup\">Sign up</button>")
    print("</a>")

    print("</div>")

else:
    print("<button id=\"user\" onclick=\"user()\">" + username + "</button")

print("</body>")

print("</html>")