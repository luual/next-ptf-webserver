from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import *
from graphene import *
from bson import ObjectId

class UserModel(Document):
    meta = {'collection': 'Users'}
    _id = ObjectIdField(default=ObjectId)
    name = StringField()
    lastname = StringField()
    userIcon = StringField()


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

class TransactionModel(Document):
    meta = {'collection': 'Transactions'}
    _id = ObjectIdField(default=ObjectId)
    walletId = StringField()
    stockId = StringField()
    quantity = DecimalField()
    stockPrice = DecimalField()
    description = StringField()