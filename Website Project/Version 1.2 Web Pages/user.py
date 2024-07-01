#!/usr/bin/python3

import http.cookies
import os

print ("Content-type: text/html\n\n")

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
username = cookie.get('username').value
token = cookie.get('token').value

print("<html>")

print("<head>")

print("<title>" + username + " Info </title>")

print("<script>")

print("function signout() {")
print("document.cookie = 'username=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=\';")
print("document.cookie = 'token=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=\';")
print("document.cookie = 'team=; expires Thu, 01 Jan 1970 00:00:00 GMT; path=\';")
print("window.location.href = 'logout.py';")
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

print("<a href=\"home.py\">")
print("<button id=\"home\">Home</button>")
print("</a>")

print("<button id=\"signout\" onclick=\"signout()\">Sign Out</button>")

print("</body>")

print("</html>")
