from dataclasses import dataclass
'''
Message Code for ticker:
3001: Ticker Price
3002: Ticker OHLC Price
'''
@dataclass
class Stock:
    id: int
    symbol: str
    mic: str
    figi: str
    description: str
    currency: str

@dataclass
class StockQuantity:
    quantity: int
    stockId: int

@dataclass
class MiniTickerMetadata:
    symbol: str
    quantity: int

@dataclass
class MiniTickerResponse():
    symbol: str
    time: float
    price:float
    messageId: int = 3001

@dataclass 
class MiniTickerOHLCResponse():
    symbol: str
    time: float
    open: float
    high: float
    low: float
    close: float
    messageId: int = 3002

