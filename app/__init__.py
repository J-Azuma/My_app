from dotenv import load_dotenv
from flask import (Flask)
from configration.database.initdb import init_db

def create_app():
    
    load_dotenv()
    app = Flask(__name__, instance_relative_config=True)
    
    # DB設定を初期化
    init_db(app)
    return app 


app = create_app()
    