from dotenv import load_dotenv
from flask import (Flask)
from app.view.user.userview import UserView
from os.path import join, dirname
import os
def create_app():
    
    load_dotenv()
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(UserView.user, url_prefix='/api/v1/users/')
    return app 


app = create_app()
