from mongoengine import Document
from mongoengine.fields import *
from bson import ObjectId

class StockModel(Document):
    """
    StockModel
    """
    meta = {'collection': 'Stocks'}
    _id = ObjectIdField(default=ObjectId)
    symbol = StringField()
    mic = StringField()
    figi =  StringField()
    description = StringField()
    currency = StringField()