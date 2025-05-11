#!/bin/bash
#build docker image
docker build -t brag:latest .
#run docker container and remove it when it stops
#run the container in detached mode
# -d: run in detached mode
# -p: publish a container's port to the host
# -rm: automatically remove the container when it exits
# -p 80:5000: map port 80 on the host to port 5000 on the container
# --name: name the container
docker run -d -p -rm 80:5000 --name brag-container brag:latest
#make sure the app actually starts
python3 app.py