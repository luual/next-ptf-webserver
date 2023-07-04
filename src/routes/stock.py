"""
Define the blueprint for stocks
"""

from flask import Blueprint
from flask_restful import Api

from ..resources import StocksResource

STOCKS_BLUEPRINT = Blueprint("stocks", __name__)
Api(STOCKS_BLUEPRINT).add_resource(StocksResource, "/stocks")