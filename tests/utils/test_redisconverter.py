'''
Test Module for redis converter
'''

from src.utils.RedisExtension import RedisDateConverter
from datetime import datetime

def test_redis_converter_timestamp_to_date():
    '''
    Test:
    
    Convert timestamp from redis to datetime
    '''
    date = RedisDateConverter.timestamp_to_datetime(1794673845185)
    assert date == datetime(2026, 11, 14, 17,30,45,185000)

def test_redis_convert_date_to_timestamp():
    '''
    Test:

    Convert datetime to redis timestamp
    '''
    d = datetime(2026, 11, 14, 17,30,45,185000)
    timestamp = RedisDateConverter.datetime_to_timestamp(d)

    assert timestamp == 1794673845185