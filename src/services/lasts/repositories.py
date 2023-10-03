""" Defines Last Repository """

import redis
from src.config import config
from src.models.Stocks import LastPrice
from src.utils.RedisExtension import RedisDateConverter
from datetime import datetime

class LastRepository:
    """ Last repository """
    def __init__(self) -> None:
        self._redis = redis.Redis(host=config['redis']['server'], port=config['redis']['port'], db=0)
    
    def lasts(self, stock: str, depth:int=None) -> list[LastPrice]:
        '''
        Get all lasts from redis.

        Returns:
            List[LastPrice]: Returns a list of all LastPrice
        '''
        ts = self._redis.ts()
        if self._redis.exists(stock) <= 0:
            return []
        output = []
        try:
            reverse = ts.revrange(stock, '-', '+', depth)
            for item in reverse:
                output.append(LastPrice(stock,
                                        item[0] / 1_000,
                                        item[1]))
            output.reverse()
        except Exception as e:
            raise Exception("Redis Repository: ", e)
        return output