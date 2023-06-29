from flask import Flask
from flask_cors import CORS
from flask_sock import Sock
import time
import json
import datetime
from src.modules.subscription import subscribe_price
from src.utils.Encoder import DataclassEncoder
from src.modules.tickers import *
from src.models.User import User
from src.models.TickerModel import MiniTickerMetadata
from src.models.Portofolio import Portfolio
from src.grql.schemas import schema
from graphql_server.flask import GraphQLView
from src.api.stocks import stock_route

app = Flask(__name__)
sock = Sock(app)
CORS(app)
app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

app.register_blueprint(stock_route, url_prefix="/api")


@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/user/random")
def random_user():
    return json.dumps(User(
        id="a349204d-5d58-4b48-bfb6-fb7fbd7ae103",
        name='Tom',
        lastname='Jerry',
        userIcon="https://images.unsplash.com/photo-1685972215665-80580c58e4ee?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2097&q=80"
    ), cls=DataclassEncoder)


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


@app.route("/users/testql")
def get_user():
    query = '''
    query {
        user(name: "Bon") {    
        id, name, userIcon
        }
    }
'''
    result = schema.execute(query)
    return result.data['user']