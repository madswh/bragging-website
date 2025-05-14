#!/bin/bash
#build docker image
docker build -t brag:latest .

#run docker image
docker run -d --rm --name brag -p 80:5001 brag:latest
