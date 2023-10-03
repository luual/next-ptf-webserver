from mongoengine import Document
from mongoengine.fields import *
from bson import ObjectId

class TransactionModel(Document):
    meta = {'collection': 'Transactions'}
    _id = ObjectIdField(default=ObjectId)
    walletId = StringField()
    stockId = StringField()
    quantity = DecimalField()
    stockPrice = DecimalField()
    description = StringField()
    executedDate = DateTimeField()