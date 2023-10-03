"""
Define the blueprint for stocks

TBD: Not sure of this design
"""

from flask import Blueprint
from flask_restful import Api

from .resources import StocksResource

STOCKS_V2_BLUEPRINT = Blueprint("stocks_v2", __name__)
Api(STOCKS_V2_BLUEPRINT).add_resource(StocksResource, "/stocks")