import urllib

class AppConfig:
    databaseUrl: str

    def __init__(self) -> None:
        self.databaseUrl = ""

appConfig = AppConfig()