import graphene

from graphene_mongo import MongoengineObjectType, MongoengineConnectionField
from graphene.relay import Node
from mongoengine import connect, DoesNotExist
from .models import *
from bson import ObjectId
from builtins import str

connect(db="portfolio-next", host="192.168.0.14:32770")


class User(MongoengineObjectType):
    class Meta:
        model = UserModel

class Stock(MongoengineObjectType):
    class Meta:
        model = StockModel
        interfaces = (Node,)


class StockQuantity(MongoengineObjectType):
    class Meta:
        model = StockQuantity
        interfaces = (Node,)

    quantity = graphene.Int()
    Stock = Stock

class Wallet(MongoengineObjectType):
    class Meta:
        model = WalletModel
        interfaces = (Node,)

    stocks = graphene.List(StockQuantity)

def resolve_wallet(wallet_id):
    wallet = WalletModel.objects.get(_id=ObjectId(wallet_id))
    stocks = []

    for stock_quantity in wallet.stocks:
        try:
            print("StockId:", stock_quantity.stock.description)
            stock = StockModel.objects.get(_id=ObjectId(stock_quantity.stock._id))
            stocks.append(StockQuantity(quantity=stock_quantity.quantity, stock=stock))
        except DoesNotExist:
            print("error does not exists")
    wallet =  Wallet(
        _id=str(wallet._id),
        userId=wallet.userId,
        name=wallet.name,
        stocks=stocks,
    )
    return wallet

class Query(graphene.ObjectType):
    users = graphene.List(User)
    user = graphene.Field(User, name=graphene.String())
    allStock = graphene.List(Stock)
    stock = graphene.Field(Stock,id=graphene.Int())
    wallets = graphene.List(Wallet)
    wallet = graphene.List(Wallet, userId=graphene.String())
    stock_by_id = graphene.Field(Stock, stock_id=graphene.String())
    wallet_by_id = graphene.Field(
        Wallet,
        wallet_id=graphene.String(),
    )
    node = Node.Field()

    def resolve_wallet_by_id(root, info, wallet_id):
        wallet = WalletModel.objects.filter(_id=ObjectId(wallet_id)).first()
        stocks = []

        for stock_quantity in wallet.stocks:
            try:
                if stock_quantity.stock:
                    print(stock_quantity.stock.description)
                    stocks.append(StockQuantity(quantity=stock_quantity.quantity, stock=stock_quantity.stock))
            except DoesNotExist:
                print("error does not exists")
        wallet =  Wallet(
            _id=str(wallet._id),
            userId=wallet.userId,
            name=wallet.name,
            stocks=stocks,
        )
        return wallet
    
    def resolve_stock_by_id(self, info, stock_id):
        try:
            stock = StockModel.objects.get(_id=ObjectId(stock_id))
            return stock
        except StockModel.DoesNotExist:
            return None
    def resolve_users(self, info):
        return list(UserModel.objects.all())

    def resolve_user(self, info, name):
        return UserModel.objects.get(name=name)
    
    def resolve_stock(self, info, id):
        return StockModel.objects.get(id=id)
    def resolve_allStock(self, info):
        return list(StockModel.objects.all())
    
    def resolve_wallets(self, info):
        walletModels = WalletModel.objects.all()
        return [resolve_wallet(wallet._id) for wallet in walletModels]

    def resolve_wallet(self, info, userId):
        return list(WalletModel.objects.filter(userId=userId))  


schema = graphene.Schema(query=Query)
