import dataclasses
import json
from decimal import Decimal

class DataclassEncoder(json.JSONEncoder):
    def default(self, o):
        if (dataclasses.is_dataclass(o)):
            return dataclasses.asdict(o)
        if (isinstance(o, Decimal)):
            return str(o)
        return super().default(o)