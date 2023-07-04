from flask import Flask
from flask_cors import CORS
from flask_sock import Sock
import time
import json
import datetime
from src.modules.subscription import subscribe_price
from src.utils.Encoder import DataclassEncoder
from src.modules.tickers import *
from src.models.TickerModel import MiniTickerMetadata
from src.models.Portofolio import Portfolio
from src.grql.schemas import schema
from src.grql.models import *
from graphql_server.flask import GraphQLView
from src.api.stocks import stock_route
from src.api import *

app = Flask(__name__)
sock = Sock(app)
CORS(app)
app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

# app.register_blueprint(stock_route, url_prefix="/api")
app.register_blueprint(wallets_route, url_prefix="/api")
# from src.routes.user import USER_BLUEPRINT
# from src.routes.stock import STOCKS_BLUEPRINT
# app.register_blueprint(USER_BLUEPRINT, url_prefix="/api")
# app.register_blueprint(STOCKS_BLUEPRINT, url_prefix="/api")

import src.routes

for blueprint in vars(src.routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint, url_prefix="/api")


@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/users/<id>/portfolio")
def get_user_portfolio(id):
    return json.dumps(
        [Portfolio(id="wqefqweqw-qweqw", name="Portfolio 1", userId=id, tickers=[
            MiniTickerMetadata("Total", 123),
            MiniTickerMetadata("CA", 22),
            MiniTickerMetadata("Air Liquid", 992),
            MiniTickerMetadata("LVMH", 1248),
            MiniTickerMetadata("L'Oreal", 57),
        ]),
            Portfolio(id="wqfw-qweqw-q123w", name="Portfolio 2", userId=id, tickers=[
                MiniTickerMetadata("Netflix", 32),
                MiniTickerMetadata("Meta", 73),
                MiniTickerMetadata("Google", 35)])], cls=DataclassEncoder)


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
    sub = subscribe_price(subRequest['symbol'])
    ws.send(json.dumps(sub, cls=DataclassEncoder))
    currentTime = time.time()
    historical = generate_historical_OHLC_ticker_values(subRequest['symbol'])
    prev_ohlc = historical[-1]
    for hdata in historical:
        ws.send(json.dumps(hdata, cls=DataclassEncoder))
    while (currentTime < sub.validTime):
        time.sleep(0.5)
        ohlc = generate_OHLC_ticker_values(
            subRequest['symbol'], refValue=prev_ohlc.close, last_date=datetime.fromtimestamp(prev_ohlc.time))
        ws.send(json.dumps(ohlc, cls=DataclassEncoder))
        prev_ohlc = ohlc
        currentTime = time.time()
    ws.close()

