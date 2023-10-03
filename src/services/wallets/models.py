from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import *
from bson import ObjectId

class StockModel(Document):
    meta = {'collection': 'Stocks'}
    _id = ObjectIdField(default=ObjectId)
    symbol = StringField()
    mic = StringField()
    figi =  StringField()
    description = StringField()
    currency = StringField()

class StockQuantity(EmbeddedDocument):
    quantity = IntField()
    stock = ReferenceField(StockModel)

class WalletModel(Document):
    meta = {'collection': 'Wallets'}
    _id = ObjectIdField(default=ObjectId)
    cash = DecimalField()
    userId = StringField()
    name = StringField()
    stocks = ListField(EmbeddedDocumentField(StockQuantity))