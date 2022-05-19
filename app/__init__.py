from dotenv import load_dotenv
from flask import (Flask)
from app.view.user.userview import UserView
from app.configration.database.initdb import init_db

def create_app():
    
    load_dotenv()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_envvar('FLASK_CONFIG')
    # DB読み込み
    init_db(app)
    app.register_blueprint(UserView.user, url_prefix='/api/v1/users/')
    
    return app 


app = create_app()
