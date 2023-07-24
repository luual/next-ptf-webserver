from flask_restful import Resource

from src.grql.models import WalletModel
from ..repositories import WalletRepository
from src.utils.mongoencoder import MongoEncoder

def GenerateWalletObject(wallet: WalletModel) -> dict:
    w = {
        "_id":str(wallet._id),
        "cash": str(wallet.cash),
        "userId": wallet.userId,
        "name": wallet.name,
        "stocks": []
    }
    for stock_quantity in wallet.stocks:
        s = {
            "_id": str(stock_quantity.stock._id),
            "symbol": stock_quantity.stock.symbol,
            "mic": stock_quantity.stock.mic,
            "figi": stock_quantity.stock.figi,
            "description": stock_quantity.stock.description,
            "currency": stock_quantity.stock.currency,
        }
        w["stocks"].append({
            "quantity": stock_quantity.quantity,
            "stock": s
        })
    return w
class WalletResource(Resource):
    def get(self, id):
        """Return wallet based on id"""
        return GenerateWalletObject(WalletRepository.get(id))
    
class UserWallerResource(Resource):
    def get(self, user_id):
        """Return user Wallets"""
        wallets = WalletRepository.get_user_wallets(user_id=user_id)
        
        output = []
        for wallet in wallets: 
            output.append(GenerateWalletObject(wallet=wallet))
        return output