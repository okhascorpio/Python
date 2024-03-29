#from distutils.command.config import config
from flask import Flask
from src.auth import auth
from src.todos import todos
from src.database import db
import os
from flask_jwt_extended import JWTManager

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            #SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY')
            
        )
        #print(os.environ.get('JWT_SECRET_KEY'))

    else:
        app.config.from_mapping(test_config)


    db.app = app
    db.init_app(app)

    JWTManager(app)

    app.register_blueprint(auth)
    app.register_blueprint(todos)

    return app
