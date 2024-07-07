#!/usr/bin/python3
#!- - - - - - - - - -!#

#TODO Import libraries needed for project
# ? Imports subprocess to use Shell commands in python.
import subprocess
#!- - - - - - - - - -!#

#TODO Start up cluster
# ? Uses Shell commands to start a minikube 4 node cluster named website.
subprocess.run("minikube start --nodes=4 --profile=website", shell=True)
subprocess.run("minikube profile website", shell=True)
#!- - - - - - - - - -!#

#TODO Set node types for the 4 nodes within my website cluster
# ? Uses Shell to se the first node in the cluster to a mysql-node type.
subprocess.run(
    "kubectl label nodes website node-type=mysql-node",
    shell=True,
)
# ? Creates a loop to set the rest of the nodes in the cluster to apache-node types.
tmp = 2
while tmp < 5:
    subprocess.run(
    "kubectl label nodes website-m0{} node-type=apache-node".format(tmp),
    shell=True,
    )
    tmp += 1
#!- - - - - - - - - -!#

#TODO Apply my yaml files which contains the deployment and service inside each file
# ? Uses Shell to apply my apache deployment and service.
subprocess.run(
    "kubectl apply -f apache.yaml",
    shell=True,
)
# ? Uses Shell to apply my mysql deployment and service.
subprocess.run(
    "kubectl apply -f mysql.yaml", shell=True
)
#!- - - - - - - - - -!#

#TODO Wait for all of the deployments to be properly rolled out onto their assigned nodes
# ? Uses Shell to wait for the apache deployment to be rolled out onto 3 ndoes.
subprocess.run("kubectl rollout status deployment/apache", shell=True)
# ? Uses Shell to wait for the mysql deployment to be rolled out onto 1 node.
subprocess.run("kubectl rollout status deployment/mysql", shell=True)
#!- - - - - - - - - -!#

# ? Starts the web server and puts the url in the current terminal.
subprocess.run("minikube service apache --url", shell=True)
