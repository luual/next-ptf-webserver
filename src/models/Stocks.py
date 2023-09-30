from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

# @dataclass
# class Stock:
#     id : str
#     symbol : str
#     mic : str
#     figi : str
#     description : str
#     currency : str

# @dataclass
# class StockQuantity:
#     quantity : int
#     stock : Stock

@dataclass
class LastPrice:
    symbol: str
    date: datetime
    last: Decimal