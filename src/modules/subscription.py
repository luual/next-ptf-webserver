from src.models.Responses import TickerSubscriptionResponse
import time
import datetime

def subscribe_price(symbol: str) -> TickerSubscriptionResponse:
    closeTime = datetime.datetime.now() + datetime.timedelta(seconds=120)

    return TickerSubscriptionResponse(symbol=symbol, open=time.time(),
                                      validTime=closeTime.timestamp(),
                                      state=True,
                                      id=1,
                                      messageId=2002)

def subscribe_ohlc_price(symbol: str) -> TickerSubscriptionResponse:
    closeTime = datetime.datetime.now() + datetime.timedelta(seconds=120)

    return TickerSubscriptionResponse(symbol=symbol, open=time.time(),
                                      validTime=closeTime.timestamp(),
                                      state=True,
                                      id=1,
                                      messageId=2002)