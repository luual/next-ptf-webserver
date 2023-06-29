from flask import Blueprint
from src.grql.schemas import schema

wallets_route = Blueprint('wallets', __name__)


@wallets_route.route("wallet/<user_id>")
def get_wallet(user_id):
    query = '''
    query {
        wallet () {
            Id
            name
                stocks {
                  quantity
                  stockId
                }
            }
        }'''
    result = schema.execute(query)
    wallet = result.data['wallet']
