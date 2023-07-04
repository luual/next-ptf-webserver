class AppConfig:
    databaseUrl: str

    def __init__(self) -> None:
        self.databaseUrl = "192.168.0.14:32770"

appConfig = AppConfig()