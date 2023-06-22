from dataclasses import dataclass
from .TickerModel import MiniTickerMetadata

@dataclass
class Portfolio:
    id: str
    userId: str
    tickers: list[MiniTickerMetadata]