from ..grql.models import TransactionModel

class TransactionRepository:
    """
    Transaction Repository
    """

    def get_wallet_transactions(wallet_id: str) -> list[TransactionModel]:
        return TransactionModel.objects.filter(walletId=wallet_id)
    
    def add_transaction(wallet_id: str,
                        stock_id: str,
                        quantity: float,
                        stock_price:float,
                        description: str=None) -> TransactionModel:
        return TransactionModel(walletId=wallet_id,
                         stockId=stock_id,
                         quantity=quantity,
                         stockPrice=stock_price,
                         description=description).save()