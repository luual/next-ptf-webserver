from flask import Flask
from flask_cors import CORS
from flask_sock import Sock
import time
import json
import datetime
from src.modules.subscription import subscribe_price
from src.utils.Encoder import DataclassEncoder
from src.modules.tickers import *
from flask import Blueprint
# from src.models.TickerModel import MiniTickerMetadata
# from src.models.Portofolio import Portfolio
from src.grql.schemas import schema
from src.grql.models import *
from graphql_server.flask import GraphQLView
from src.api import *
import src.routes

app = Flask(__name__)
sock = Sock(app)
CORS(app)
app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

for blueprint in vars(src.routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint, url_prefix="/api")

from src.services.stocks.routes import *

app.register_blueprint(STOCKS_V2_BLUEPRINT, url_prefix="/api/v2")

##
## Legacy Code
##

@app.route("/")
def hello():
    return "Hello, World!"

@sock.route("/ticker")
def send_ticker(ws):
    config = ws.receive()
    subRequest = json.loads(config)
    sub = subscribe_price(subRequest['symbol'])
    ws.send(json.dumps(sub, cls=DataclassEncoder))
    currentTime = time.time()
    historical = generate_historical_ticker_values(subRequest['symbol'])
    for hdata in historical:
        ws.send(json.dumps(hdata, cls=DataclassEncoder))
    while (currentTime < sub.validTime):
        time.sleep(0.5)
        ws.send(json.dumps(generate_ticker_values(
            subRequest['symbol']), cls=DataclassEncoder))
        currentTime = time.time()
    ws.close()


@sock.route("/ticker/ohlc")
def send_ticker_ohlc(ws):
    config = ws.receive()
    subRequest = json.loads(config)
    symbol = subRequest['symbol']
    sub = subscribe_price(symbol)
    ws.send(json.dumps(sub, cls=DataclassEncoder))
    currentTime = time.time()
    historical = get_hprice_from_symbol(symbol, None)
    print(historical)
    if len(historical) > 0:
        prev_ohlc = historical[-1]
        for hdata in historical:
            ws.send(json.dumps(hdata, cls=DataclassEncoder))
    else:
        open, close, high, low = generate_OHLC()
        prev_ohlc = MiniTickerOHLCResponse(symbol=symbol, time=datetime.now().timestamp(),
                                           open=open, high=high, low=low, close=close)
    while (currentTime < sub.validTime):
        time.sleep(0.5)
        ohlc = generate_OHLC_ticker_values(symbol, refValue=prev_ohlc.close, last_date=datetime.fromtimestamp(prev_ohlc.time))
        add_and_publish_to_redis(symbol=symbol, ohlc=ohlc)
        ws.send(json.dumps(ohlc, cls=DataclassEncoder))
        prev_ohlc = ohlc
        currentTime = time.time()
    ws.close()

from src.manager.redis import Manager

@app.route("/redis/time")
def send_redis_time():
    r = Manager()
    t = datetime.now().isoformat()
    r.publish(t)
    return t


@app.route("/redis/time2")
def send_redis_time2():
    r = Manager()
    t = datetime.now().isoformat()
    r.publish(t, "channel2")
    return t

import redis

def get_or_create_last_symbol_tick(symbol: str) -> (datetime, float):
    r = redis.Redis(host='localhost', port=6379, db=0)
    ts = r.ts()
    if r.exists(symbol) > 0:
        last = ts.get(symbol)
        return (datetime.fromtimestamp(last[0] / 1000, last[1]))
    else:
        ts.create(symbol)
        return (datetime.now().timestamp(), random.randrange(1,9999))

def get_hprice_from_symbol(symbol: str, depth:int = 10) -> list[MiniTickerOHLCResponse]:
    r = redis.Redis(host='localhost', port=6379, db=0)
    ts = r.ts()
    output = []
    if r.exists(symbol) > 0:
        reversed = ts.revrange(symbol, '-', '+', depth)
        for item in reversed:
            output.append(MiniTickerOHLCResponse(symbol=symbol,
                                                time=item[0] / 1_000,
                                                high=0,
                                                low=0,
                                                open=0,
                                                close=item[1]))
        output.reverse()
    return output

def add_and_publish_to_redis(symbol:str, ohlc: MiniTickerOHLCResponse):
    r = redis.Redis(host='localhost', port=6379, db=0)
    ts = r.ts()
    ts.add(symbol, int(ohlc.time * 1_000), ohlc.close)