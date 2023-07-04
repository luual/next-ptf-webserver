""" Defines wallet repository """

from ..grql.models import WalletModel, StockQuantity
from bson import ObjectId

class WalletRepository:
    """Wallet Repository """
    def gets() -> list[WalletModel]:
        """Returns all wallets"""
        return WalletModel.objects.all()
    
    def get(wallet_id: str) -> WalletModel:
        """ Return single wallet based on id"""
        return WalletModel.objects.first(_id=ObjectId(wallet_id))
    
    def get_user_wallets(user_id: str) -> list[WalletModel]:
        """ Returns user wallets"""
        return WalletModel.objects.filter(user_id=user_id)