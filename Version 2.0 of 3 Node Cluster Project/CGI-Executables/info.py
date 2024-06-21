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
# ? Use Shell commands to grab all the variables needed to identify what node is hosting the server.
node = (subprocess.run("echo $NODE_NAME", shell=True, capture_output=True, text=True)).stdout.strip()
pod_file = open('/etc/hostname', 'r')
pod = pod_file.read()
ip = (subprocess.run(
    "hostname -i", shell=True, capture_output=True, text=True
)).stdout.strip()
#node = "Server"
#pod = "apache"
#ip = "127.0.0.1"
#!- - - - - - - - - -!#

#TODO Print out all of the variables.
print(node)
print(ip)
print(pod)
#!- - - - - - - - - -!#

#TODO Close opened files.
pod_file.close()