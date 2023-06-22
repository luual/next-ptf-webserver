from dataclasses import dataclass
from .Responses import Response

'''
Message Code for ticker:
3001: Ticker Price
3002: Ticker OHLC Price
'''


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

