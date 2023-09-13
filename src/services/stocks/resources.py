from flask_restful import Resource
from .repositories import StockRepository
from src.utils.mongoencoder import MongoEncoder

class StocksResource(Resource):
    def get(self) -> list[dict]:
        """ Returns all Stocks """
        stocks = StockRepository.get_all()
        output = []
        for stock in stocks:
            output.append(MongoEncoder(stock).to_dict())
        return output