#!/usr/bin/python3
#!- - - - - - - - - -!#

#TODO Makes sure that the python code can be executed as an html file.
# ? Allows my python code to execute as an html file.
print ("Content-type: text/html\n\n")
#!- - - - - - - - - -!#

#TODO Open and read the node.txt and pod.txt files that includes
#TODO the name of the pod and the node it is located on.
print("<html>")
node_file = open('/tmp/node.txt', 'r')
read = node_file.read()
#read = "You are on node: 2"
# ? Runs a for loop to find what node number this pod is on.
for words in read:
    if words.isdigit():
        node = int(words)
        #print(node)
# ? Opens the pod.txt and print out what the name of the pod is to the website.
pod_file = open('/tmp/pod.txt', 'r')
pod = pod_file.read()
#node = 3
#!- - - - - - - - - -!#

#TODO Depending on what node this pod is located on change the color
#TODO of the website to a distinct color.
print("<head>")
print("<style>")
print("body{")
print("color: white;text-align: center;margin: 0;padding: 20px;")
# ? If, elif, else statement to change the color of the background depending
# ? on what node is hosting the server.
if node == 3:
    print("background-color: green;")
elif node == 2:
    print("background-color: blue;")
else:
    print("background-color: red;")
print("}")
print("</style>")
print("</head>")
#!- - - - - - - - - -!#

#TODO Print out information of what node is hosting the server and what pod is being displayed.
print("<body>")
print("<h1>")
print("Hello from node: ")
print(node)
print("</h1>")
print("<p>")
print("You are in pod: ")
print(pod)
print("</p>")
print("</body>")
print("<html>")
#!- - - - - - - - - -!#

#TODO Close opened files.
node_file.close()
pod_file.close()