import urllib

class AppConfig:
    databaseUrl: str

    def __init__(self) -> None:
        self.databaseUrl = "mongodb+srv://mongo-ptf:" + urllib.parse.quote("NPbVuaH4whukIWC5")+"@cluster0.hhlpnp3.mongodb.net/?retryWrites=true&w=majority"

appConfig = AppConfig()