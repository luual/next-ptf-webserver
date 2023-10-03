from flask_restful import Resource
from .repositories import UserRepository
from src.utils.mongoencoder import MongoEncoder

class UserResource(Resource):
    def get(self):
        """ Return first user"""
        user = UserRepository.get_first()
        return MongoEncoder(user).to_dict()
