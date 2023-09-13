import redis 

class Manager:
    def __init__(self) -> None:
        self.__redis = redis.Redis(host='localhost', port=6379, db=0)


    def publish(self, message: str, channel:str="channel1"):
        self.__redis.publish(channel, message)