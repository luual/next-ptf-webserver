from src.grql.models import *
from src.utils.mongoencoder import *

def test_mongoencoder():
    transaction = TransactionModel(_id="eewwq",
                                   walletId="qwe",
                                   stockId="qwe",
                                   quantity=123,
                                   stockPrice=2222.2,
                                   description="")
    d = MongoEncoder(transaction).to_dict()
    assert d['_id'] == "eewwq"
    assert d['walletId'] == "qwe"
    assert d['stockId'] == "qwe"
    assert d['quantity'] == 123
    assert d['stockPrice'] == 2222.2
    assert d['description'] == ''