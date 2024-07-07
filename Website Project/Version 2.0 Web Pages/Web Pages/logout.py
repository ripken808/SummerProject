#!/usr/bin/python3
#!- - - - - - - - - -!#

#TODO Makes sure that the python code can be executed as an html file
# ? Allows my python code to execute as an html file.
print ("Content-type: text/html\n\n")
#!- - - - - - - - - -!#

#TODO Use Html code to display content
print("<html>")

print("<style>")
# ? Centers the text inside of h1 to the center of the page.
print("h1{")
print("position: absolute;")
print("top: 50%;")
print("left: 50%;")
print("transform: translate(-50%,-50%);")
print("font-family: Verdana, Geneva, Tahoma, sans-serif;")
print("font-size: 50px;")
print("}")
# ? Sets the home button to the top left of the web page.
print("#home{")
print("border-radius: 10px;")
print("position: absolute;")
print("margin-top: 0;")
print("}")

print("</style>")

print("<head>")

print("</head>")
# ? Sets the body color to a dark purple color.
print("<body bgcolor=\"#1a0d54\">")
# ? Creates a home button that links to the home page of my web page.
print("<a href=\"home.py\">")
print("<button id=\"home\">Home</button>")
print("</a>")
# ? Lets the user know that they have been sign out and their cookies have been cleared.
print("<h1 style=\"color: white\">You have been successfully signed out</h1>")

print("</body>")

print("</html>")