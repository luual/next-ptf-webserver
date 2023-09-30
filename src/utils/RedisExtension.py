'''Extension module for Redis lib'''

from datetime import datetime


class RedisDateConverter():
    def __init__(self) -> None:
        pass

    def timestamp_to_datetime(timestamp: float) -> datetime:
        '''
        Convert redis timestamp to correct datetime

        Input:
            - timestamp: redis timestamp

        Returns:
            datetime: Converted timestamp to datetime
        '''
        return datetime.fromtimestamp(timestamp / 1_000)
    
    def datetime_to_timestamp(date: datetime) -> float:
        '''
        Convert datetime to redis timestamp

        Input: 
            - date: datetime

        Returns: Converted date as float timestamp
        '''

        return date.timestamp() * 1_000