#!/bin/bash
#build docker image
docker build -t brag:latest .
docker run -rm 5001:5001 --name brag-container brag:latest
#make sure the app actually starts
python3 app.py