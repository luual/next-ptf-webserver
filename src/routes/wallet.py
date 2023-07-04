"""
Defines the blueprint for wallets
"""

from flask import Blueprint
from flask_restful import Api

from ..resources import WalletResource, UserWallerResource

WALLET_BLUEPRINT = Blueprint("wallet", __name__)
USER_WALLET_BLUEPRINT = Blueprint("user_wallet", __name__)

Api(WALLET_BLUEPRINT).add_resource(WalletResource, "/wallets/<id>")
Api(USER_WALLET_BLUEPRINT).add_resource(UserWallerResource, "/wallets/users/<user_id>")