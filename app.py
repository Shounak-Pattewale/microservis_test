from config import DefaultConfig

from flask import Flask, request, jsonify

from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended import JWTManager

from flask_bcrypt import Bcrypt
from flask_restful import Api

from db import initialize_db
from db.basic_errors import basic_errors

from routes import initialize_routes

app = Flask(__name__)       # Initializing app

app.config.from_object(DefaultConfig)       # Loading default configuration

initialize_db(app)      # Initializing database connection

collective_errors = {**basic_errors}        # Initializing basic errors     
api = Api(app, errors=collective_errors)        # Initializing API

initialize_routes(api)      # Initializing routes

bcrypt = Bcrypt(app)        # Bcrypt initializing (authorization)
jwt = JWTManager(app)       # JWT initializing (authorization)


if __name__ == '__main__':
    app.run()