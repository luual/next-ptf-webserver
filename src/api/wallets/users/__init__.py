from ...wallets import wallets_route, query_wallet
from src.models.Stocks import *
from src.models.Wallets import *
from src.utils.Encoder import DataclassEncoder
import src.grql.models as mongoModels
from src.utils.Encoder import DataclassEncoder
import json
from mongoengine import connect
from src.config import appConfig

connect(db="portfolio-next", host=appConfig.databaseUrl)

@wallets_route.route("wallets/users/<user_id>")
def get_user_wallet(user_id):
    walletsDb = mongoModels.WalletModel.objects.filter(userId=user_id)
    results = [query_wallet(wallet._id) for wallet in walletsDb]
    return json.dumps(results, cls=DataclassEncoder)