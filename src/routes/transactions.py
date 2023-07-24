"""
Define the bluerpint for transaction
"""

from flask import Blueprint
from flask_restful import Api

from ..resources import TransactionResource

TRANSACTION_BLUEPRINT = Blueprint("transactions", __name__)
Api(TRANSACTION_BLUEPRINT).add_resource(TransactionResource, "/transactions/<wallet_id>")