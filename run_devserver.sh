#!/bin/bash

service mysql start
export FLASK_APP=app 
export FLASK_ENV=development
export APP_CONFIG=/usr/local/my_app/config/dev.py
flask run