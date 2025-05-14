#!/bin/bash
git pull
#build docker image
docker build -t brag:latest .

#run docker image
docker run --rm -d -p 80:5001 brag:latest