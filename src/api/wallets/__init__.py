from flask import Blueprint
from src.grql.schemas import schema, resolve_wallet
from src.models.Stocks import *
from src.models.Wallets import *
from src.utils.Encoder import DataclassEncoder
import json

wallets_route = Blueprint('wallets', __name__)


@wallets_route.route("wallets/<wallet_id>")
def get_wallet(wallet_id):
    print(wallet_id)

    wallet = resolve_wallet(str(wallet_id))
    print(wallet)
    stocks = []
    for stock_quantity in wallet.stocks:
        print(str(stock_quantity.stock._id))
        stock = StockQuantity(quantity=stock_quantity.quantity,
                              stock=Stock(id=str(stock_quantity.stock._id),
                                    symbol=stock_quantity.stock.symbol,
                                    mic=stock_quantity.stock.mic,
                                    figi=stock_quantity.stock.figi,
                                    description=stock_quantity.stock.description,
                                    currency=stock_quantity.stock.currency))
        stocks.append(stock)
    wallet =  Wallet(id=str(wallet._id),
                  userId=wallet.userId,
                  name=wallet.name,
                  stocks=stocks)
    print(wallet)
    return json.dumps(wallet, cls=DataclassEncoder)