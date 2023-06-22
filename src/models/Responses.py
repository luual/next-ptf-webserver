from dataclasses import dataclass

@dataclass
class Response:
    messageId: int

@dataclass
class TickerSubscriptionResponse(Response):
    symbol: str
    open: float
    validTime: float
    state: bool
    id:int