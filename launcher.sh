#!/bin/bash
cd /Users/maddywhitney/Documents-local/bragging-website
gunicorn -w 4 -b 0.0.0.0:5002 app:application

