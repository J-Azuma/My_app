from dotenv import load_dotenv
from flask import (Flask)

def create_app():
    
    load_dotenv()
    app = Flask(__name__, instance_relative_config=True)
    
    return app 


app = create_app()
