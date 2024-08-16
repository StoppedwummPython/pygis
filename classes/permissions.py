class Permission:
    def __init__(self, info: dict, name: str) -> None:
        self.PermName = name
        self.allowed: bool = info["allowed"]
        self.fields = info["fields"]
        self.constraints: dict = info["constraints"]
