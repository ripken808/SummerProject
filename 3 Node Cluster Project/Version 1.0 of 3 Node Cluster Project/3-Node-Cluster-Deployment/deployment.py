#!/usr/bin/python3
#!- - - - - - - - - -!#

# ? Imports subprocess to use Shell commands in python.
import subprocess
# ? Imports re to use regex commands.
import re
#!- - - - - - - - - -!#

# ? Uses Shell commands to start a minikube 3 node cluster.
subprocess.run("minikube start --nodes 3", shell=True)
subprocess.run("sleep 5", shell=True)
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
# ? Uses Shell to store the information of which pod is located on which node into the variable pod.
pod = subprocess.run(
    "kubectl get pods -o wide", shell=True, capture_output=True, text=True
)
# ? Gets rid of excess whtie spaces.
podInfo = pod.stdout.strip()
# print(podInfo)
#!- - - - - - - - - -!#

# ? Creates lists to store the three pods and nodes.
pods = []
nodes = []
# ? Uses counter node to counter how many times to loop.
node = 0
#!- - - - - - - - - -!#

# ? Uses for loop to grab the pod name and node name on each line and save it into a list
# ? that will later be inserted into text files inside of each pod.
for line in podInfo.splitlines():
    podName = re.search(r"\S+", line)
    nodeName = re.search(r"\b-m\d\d+\b", line)
    # print(nodeName)
    # print(podName.group())
    if podName is not None:
        if podName.group() != "NAME":
            node += 1
            pods.append(podName.group())
            if nodeName is not None:
                nodes.append(nodeName.group()[-1])
            else:
                nodes.append(1)
# print(pods)
# print(nodes)
#!- - - - - - - - - -!#

# ? Resets the counter
node = 0
# ? Uses a for loop that will grab every pod name and node number in their lists
# ? and will store them into two text files located on the host device.
# ? Then it will copy the text files into the already injected text files
# ! (Text files injected during docker build stage)
# ? inside of each pod. 
for num in nodes:
    subprocess.run("echo 'You are on node: '" + str(num) + "> node.txt", shell=True)
    subprocess.run("echo 'You are on node: '" + str(num), shell=True)
    subprocess.run("echo ''" + pods[node] + "> pod.txt", shell=True)
    subprocess.run("echo ''" + pods[node], shell=True)
    subprocess.run(
        "kubectl cp node.txt "
        + pods[node]
        + ":/tmp/node.txt",
        shell=True,
    )
    subprocess.run(
        "kubectl exec -it "
        + pods[node]
        + " -- cat /tmp/node.txt",
        shell=True,
    )
    subprocess.run("sleep 2", shell=True)
    subprocess.run(
        "kubectl cp pod.txt "
        + pods[node]
        + ":/tmp/pod.txt",
        shell=True,
    )
    subprocess.run(
        "kubectl exec -it "
        + pods[node]
        + " -- cat /tmp/pod.txt",
        shell=True,
    )
    subprocess.run("sleep 2", shell=True)
    node += 1
#!- - - - - - - - - -!#

# ? Starts the web server and puts the url in the current terminal.
subprocess.run("minikube service apache --url", shell=True)
