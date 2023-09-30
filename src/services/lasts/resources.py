'''
Resource module for Last service
'''

from flask_restful import Resource
from src.services.lasts.repositories import LastRepository
from src.utils.Encoder import DataclassEncoder
import json


class LastResource(Resource):
    def get(self, symbol: str) -> any:
        '''
        Get all last price for a symbol

        Inputs:
            - symbol: Requested symbol
        
        Returns:
            List of last price
        '''
        lasts = LastRepository().lasts(symbol)
        return json.loads(json.dumps(lasts, cls=DataclassEncoder))

class LastDepthResource(Resource):
    def get(self, symbol: str, depth: int) -> any:
        '''
        Get N last price for a symbol

        Inputs:
            - symbol: Requested symbol
            - depth: number of last element
        
            Returns:
                List of last price
        '''
        lasts = LastRepository().lasts(symbol, depth)
        return json.loads(json.dumps(lasts, cls=DataclassEncoder))