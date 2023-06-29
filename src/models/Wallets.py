from dataclasses import dataclass
from .Stocks import *

@dataclass
class Wallet:
    id : str
    userId : str
    name : str
    stocks : list[Stock]
