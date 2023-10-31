from flask_restful import Resource
from .repositories import UserRepository

class UserResource(Resource):
    def get(self):
        """ Return first user"""
        user = UserRepository.get_first()
        return user.as_dict()
    
