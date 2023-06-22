from src.models.TickerModel import *

def test_dataclass_generation():
    reponse = MiniTickerResponse(symbol="123", time=222, price=232)
    assert reponse.messageId == 3001