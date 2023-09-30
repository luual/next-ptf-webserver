""" Defines Stock Repository """

from src.grql.models import StockModel
from bson import ObjectId
from mongoengine import connect
from src.config import config

connect(db="portfolio-next", host=config['mongodb']['host'])

class StockRepository:
    """Stocks Repository"""
    def get(id: str) -> StockModel:
        """ query Stock Id """
        return StockModel.objects.first(id=ObjectId(id))
    
    def get_all() -> list[StockModel]:
        """ query all Stock Id """
        return StockModel.objects.all()