#!/bin/bash

service mysql start
export FLASK_APP=app 
export FLASK_ENV=development
flask run