import dataclasses
import json
from decimal import Decimal
from bson import ObjectId
from datetime import date, datetime
from mongoengine.fields import *

class DataclassEncoder(json.JSONEncoder):
    def default(self, o):
        if (dataclasses.is_dataclass(o)):
            return dataclasses.asdict(o)
        if (isinstance(o, Decimal)):
            return str(o)
        if (isinstance(o, ObjectId)):
            return str(o)
        if (isinstance(o, datetime)):
            return str(o)
        if (isinstance(o, date)):
            return str(o)
        return super().default(o)