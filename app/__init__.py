from flask import Flask, jsonify
from config import Config
from app.extension import db, migrate, bcrypt

from app.models import authentication_model

import pymysql

from flask_smorest import Api

from app.blueprint.authentication_blueprint import authentication_blp

pymysql.install_as_MySQLdb()



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    api = Api(app)
    api.register_blueprint(authentication_blp)


    @app.route('/')
    def home():
        return jsonify({"message": "Hello World"})

    return app