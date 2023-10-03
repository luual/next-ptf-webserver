from mongoengine import Document
from mongoengine.fields import *
from bson import ObjectId

class UserModel(Document):
    meta = {'collection': 'Users'}
    _id = ObjectIdField(default=ObjectId)
    name = StringField()
    lastname = StringField()
    userIcon = StringField()