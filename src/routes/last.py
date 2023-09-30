'''
Route module for Last Service
'''

from flask import Blueprint
from flask_restful import Api
from src.services.lasts.resources import LastResource, LastDepthResource

LAST_BLUEPRINT = Blueprint('last', __name__)
LAST_DEPTH_BLUEPRINT = Blueprint('last_depth', __name__)

Api(LAST_BLUEPRINT).add_resource(LastResource, "/lasts/<symbol>/")
Api(LAST_DEPTH_BLUEPRINT).add_resource(LastDepthResource, "/lasts/<depth>/<symbol>/")