from flask_restful import Resource
from ..repositories import WalletRepository
from src.utils.mongoencoder import MongoEncoder

class WalletResource(Resource):
    def get(self, id):
        """Return wallet based on id"""
        return WalletRepository.get(id)
    
class UserWallerResource(Resource):
    def get(self, user_id):
        """Return user Wallets"""
        return WalletRepository.get_user_wallets(user_id=user_id)