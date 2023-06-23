from mongoengine import Document
from mongoengine.fields import StringField

class UserModel(Document):
    meta = {'collection': 'Users'}
    _id = StringField()
    id = StringField()
    name = StringField()
    lastname = StringField()
    userIcon = StringField()