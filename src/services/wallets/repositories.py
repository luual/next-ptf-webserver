""" Defines wallet repository """

from .models import WalletModel, StockQuantity, StockModel
from bson import ObjectId

class WalletRepository:
    """Wallet Repository """
    def gets() -> list[WalletModel]:
        """Returns all wallets"""
        return WalletModel.objects.all()
    
    def get(wallet_id: str) -> WalletModel:
        """ Return single wallet based on id"""
        return WalletModel.objects.filter(_id=ObjectId(wallet_id)).first()
    
    def get_user_wallets(user_id: str) -> list[WalletModel]:
        """ Returns user wallets"""
        return WalletModel.objects.filter(userId=user_id)
    
    def add_stock(wallet_id:str, stock_id: str, quantity: int, stock_price: float) -> WalletModel:
        """ Add stock to the wallet"""
        stock = StockModel.objects.get(id=ObjectId(stock_id))
        wallet = WalletModel.objects.get(id=ObjectId(wallet_id))
        full_price = quantity * stock_price
        if (wallet.cash > full_price):
            pass