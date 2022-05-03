from flask_sqlalchemy import SQLAlchemy

# データベース接続設定を記述
db = SQLAlchemy()

# DB設定を初期化
def init_db(app):
    db.init_app(app)