""" Defines Stock Repository """

from src.grql.models import StockModel
from bson import ObjectId

class StockRepository:
    """Stocks Repository"""
    def get(id: str) -> StockModel:
        """ query Stock Id """
        return StockModel.objects.first(id=ObjectId(id))
    
    def get_all() -> list[StockModel]:
        """ query all Stock Id """
        return StockModel.objects.all()