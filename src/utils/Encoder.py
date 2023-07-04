import dataclasses
import json
from decimal import Decimal
from bson import ObjectId

class DataclassEncoder(json.JSONEncoder):
    def default(self, o):
        if (dataclasses.is_dataclass(o)):
            return dataclasses.asdict(o)
        if (isinstance(o, Decimal)):
            return str(o)
        if (isinstance(o, ObjectId)):
            return str(o)
        return super().default(o)