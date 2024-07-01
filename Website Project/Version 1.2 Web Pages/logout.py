#!/usr/bin/python3

print ("Content-type: text/html\n\n")

print("<html>")

print("<style>")

print("h1{")
print("position: absolute;")
print("top: 50%;")
print("left: 50%;")
print("transform: translate(-50%,-50%);")
print("font-family: Verdana, Geneva, Tahoma, sans-serif;")
print("font-size: 50px;")
print("}")

print("#home{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("}")

print("</style>")

print("<head>")

print("</head>")

print("<body bgcolor=\"#1a0d54\">")

print("<a href=\"home.py\">")
print("<button id=\"home\">Home</button>")
print("</a>")

print("<h1 style=\"color: white\">You have been successfully signed out</h1>")

print("</body>")

print("</html>")