from dataclasses import dataclass

@dataclass
class Stock:
    id : str
    symbol : str
    mic : str
    figi : str
    description : str
    currency : str

@dataclass
class StockQuantity:
    quantity : int
    stock : Stock
