#!/bin/bash
#build docker image
docker build -t myapp:latest .
#run docker container
docker run -d -p 80:5001 --name myapp-container myapp:latest
#make sure the app actually starts
python3 app.py