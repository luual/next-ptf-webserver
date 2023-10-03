from flask_restful import Resource, reqparse
from .repositories import TransactionRepository
from src.utils.mongoencoder import MongoEncoder

parser = reqparse.RequestParser()
parser.add_argument('stockId', type=str)
parser.add_argument('quantity', type=float)
parser.add_argument('stockPrice', type=float)
parser.add_argument('description', type=str)

class TransactionResource(Resource):
    def get(self, wallet_id):
        '''Get transactions for wallet'''
        transactions =  TransactionRepository.get_wallet_transactions(wallet_id)
        return [MongoEncoder(transaction).to_dict() for transaction in transactions]
    
    def post(self, wallet_id):
        '''
        '''
        args = parser.parse_args()
        transaction = TransactionRepository.add_transaction(wallet_id=wallet_id,
                                              stock_id=args['stockId'],
                                              quantity=args['quantity'],
                                              stock_price=args['stockPrice'],
                                              description=args['description'])        
        return MongoEncoder(transaction).to_dict()