from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from db.basic_errors import InternalServerError, SchemaValidationError, NoAuthorizationError
from mongoengine.errors import FieldDoesNotExist, ValidationError, DoesNotExist
from datetime import timedelta
import const as const

class UserLoginApi(Resource):
    def get(self):
        try:
            access_token = create_access_token(identity='str(user.id)', expires_delta=timedelta(False))
            return {'token': access_token}, const.STATUS_OK_200
        except DoesNotExist:
            raise NoUserFoundError