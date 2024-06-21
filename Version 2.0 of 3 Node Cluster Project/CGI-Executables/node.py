#!/usr/bin/python3
#!- - - - - - - - - -!#

#TODO Import libraries needed for project
# ? Imports subprocess to use Shell commands in python.
import subprocess
#!- - - - - - - - - -!#

#TODO Makes sure that the python code can be executed as an html file.
# ? Allows my python code to execute as an html file.
print ("Content-type: text/html\n\n")
#!- - - - - - - - - -!#

#TODO Store the values of pod name, node, node number, and internal ip into variables.
print("<html>")
# ? Use Shell commands to grab all the variables needed to identify what node is hosting the server.
node = (subprocess.run("echo $NODE_NAME", shell=True, capture_output=True, text=True)).stdout.strip()
#node = "server-m02"
if node[-1].isdigit():
    nodeNum = int(node[-1])
else:
    nodeNum = 1
pod_file = open('/etc/hostname', 'r')
pod = pod_file.read()
#pod = "apache-6f78f7d689-mqcqv"
ip = (subprocess.run(
    "hostname -i", shell=True, capture_output=True, text=True
)).stdout.strip()
#ip = "10.244.2.2"
#!- - - - - - - - - -!#

#TODO Depending on what node this pod is located on change the color
#TODO of the website to a distinct color.
print("<head>")
# ? Change the title of the page to include all of the important information to know
# ? what node is hosting the server.
print("<title>")
print("pod: " + pod)
print("node: " + node)
print("ip: " + ip)
print("</title>")
print("<style>")
print("body{")
print("color: white;text-align: center;margin: 0;padding: 20px;")
# ? If, elif, else statement to change the color of the background depending
# ? on what node is hosting the server.
if nodeNum == 3:
    print("background-color: green;")
elif nodeNum == 2:
    print("background-color: blue;")
else:
    print("background-color: red;")
print("}")
print("</style>")
print("</head>")
#!- - - - - - - - - -!#

#TODO Print out "Hello World!".
print("<body>")
print("<h1>")
print("Hello World!")
print("</h1>")
print("</body>")
print("</html>")
#!- - - - - - - - - -!#

#TODO Close opened files.
pod_file.close()