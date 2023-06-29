from src.models.TickerModel import *
import random
from datetime import datetime, timedelta


def generate_historical_ticker_values(ticker_name: str, depth: int = 10) -> list[MiniTickerResponse]:
    days = [i + 1 for i in range(depth)]
    output = []
    dates = [datetime.now() + timedelta(days=-i) for i in days]
    dates.sort()
    for date in dates:
        rd = random.randrange(1, 9999)
        output.append(MiniTickerResponse(symbol=ticker_name, time=date.timestamp(), price=rd))
    return output


def generate_ticker_values(ticker_name: str, last_date: datetime = None) -> MiniTickerResponse:
    rd = random.randrange(1, 9999)
    date = datetime.now()
    if last_date is not None:
        date = last_date + timedelta(days=1)
    return MiniTickerResponse(symbol=ticker_name, time=date.timestamp(), price=rd)



'''
OHLC Version
'''

def generate_historical_OHLC_ticker_values(ticker_name: str, depth: int = 10) -> list[MiniTickerOHLCResponse]:
    days = [i + 1 for i in range(depth)]
    output = []
    dates = [datetime.now() + timedelta(days=-i) for i in days]
    dates.sort()
    refValue = random.randrange(1,9999)
    for date in dates:
        ohlc = generate_OHLC_ticker_values(ticker_name=ticker_name, refValue=refValue)
        ohlc.time = date.timestamp()
        refValue = ohlc.close
        output.append(ohlc)
    return output


def generate_OHLC_ticker_values(ticker_name: str, refValue: float = random.randrange(1, 9999), last_date: datetime = None) -> MiniTickerOHLCResponse:

    open = refValue
    delta_change = random.randrange(1,20) / 100 * refValue
    pos_neg = random.randrange(0,2)
    close = refValue + delta_change if pos_neg == 1 else refValue - delta_change
    low = min([open, close]) - delta_change * (1 - (random.randrange(1, 20) / 100))
    high = max([open, close]) + delta_change * (1 + (random.randrange(1, 20) / 100))
    date = datetime.now()
    if last_date is not None:
        date = last_date + timedelta(days=1)
    return MiniTickerOHLCResponse(symbol=ticker_name, time=date.timestamp(),
                                  close=close,
                                  open=open,
                                  low=low,
                                  high=high)

