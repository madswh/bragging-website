#!/bin/bash
cd /Users/maddywhitney/Documents-local/bragging-website
echo "Starting the server... press Ctrl+C to stop it"
gunicorn -w 4 -b 0.0.0.0:5001 app:application

