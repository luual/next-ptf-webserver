from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import *
from graphene import *

class UserModel(Document):
    meta = {'collection': 'Users'}
    _id = StringField()
    name = StringField()
    lastname = StringField()
    userIcon = StringField()


class StockModel(Document):
    meta = {'collection': 'Stocks'}
    _id = StringField()
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
    _id = StringField()
    cash = DecimalField()
    userId = StringField()
    name = StringField()
    stocks = ListField(EmbeddedDocumentField(StockQuantity))