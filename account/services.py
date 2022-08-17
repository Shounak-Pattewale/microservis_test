from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from db.basic_errors import InternalServerError, SchemaValidationError, NoAuthorizationError
from mongoengine.errors import FieldDoesNotExist, ValidationError, DoesNotExist
from datetime import timedelta
import const as const

class UserLoginApi(Resource):
    def post(self):
        try:
            username = request.json.get("username", None)
            password = request.json.get("password", None)
            if username != "test" or password != "test":
                return jsonify({"msg": "Bad username or password"}), 401    
            access_token = create_access_token(identity=username)
            return {'token': access_token}, const.STATUS_OK_200
        except DoesNotExist:
            raise NoUserFoundError

    @jwt_required()
    def get(self):
        '''
        Protect a route with jwt_required, which will kick out requests
        '''
        try:
            current_user = get_jwt_identity()       # Access the identity of the current user with get_jwt_identity
            return {"logged_in_as":current_user}, const.STATUS_OK_200
        except DoesNotExist:
            raise NoUserFoundError                        