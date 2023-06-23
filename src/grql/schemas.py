import graphene

from graphene_mongo import MongoengineObjectType
from mongoengine import connect
from .models import *

connect(db="portfolio-next",host="127.0.0.1:32768")

class User(MongoengineObjectType):
    class Meta:
        model = UserModel

class Query(graphene.ObjectType):
    users = graphene.List(User)
    user = graphene.Field(User, name=graphene.String())
    
    def resolve_users(self, info):
    	return list(UserModel.objects.all())
    
    def resolve_user(self, info, name):
        return UserModel.objects.get(name=name)

schema = graphene.Schema(query=Query)