#!/usr/bin/python3
#!- - - - - - - - - -!#

#TODO Import libraries needed for project
# ? Imports subprocess to use Shell commands in python.
import subprocess
#!- - - - - - - - - -!#

#TODO Start up cluster
# ? Uses Shell commands to start a minikube 3 node cluster named server.
subprocess.run("minikube start --nodes=3 -p=server", shell=True)
#subprocess.run("sleep 5", shell=True)
subprocess.run("minikube profile server", shell=True)
# ? Uses Shell to apply my apache deployment and service.
subprocess.run(
    "kubectl apply -f apache-deployment.yaml",
    shell=True,
)
subprocess.run(
    "kubectl apply -f apache-service.yaml", shell=True
)
# ? Uses Shell to wait for all 3 pods to be spread out onto all 3 nodes.
subprocess.run("kubectl rollout status deployment/apache", shell=True)
#!- - - - - - - - - -!#

# ? Starts the web server and puts the url in the current terminal.
subprocess.run("minikube service apache --url", shell=True)
