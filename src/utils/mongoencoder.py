from mongoengine import *
import json
from .Encoder import DataclassEncoder

class MongoEncoder:
    __document: Document
    def __init__(self, document: Document):
        if document is None:
            raise Exception("Document cannot be None")
        self.__document = document

    def to_dict(self):
        return json.loads(json.dumps(self.__document.to_mongo(), cls=DataclassEncoder))
