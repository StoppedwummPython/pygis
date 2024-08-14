import json
class DockerInfo:
     def __init__(self, dI: dict) -> None:
          self.version: str = dI["version"]
          self.sourceCode = dI["sourceCode"]
          self.author: str = dI["author"]
          self.dockerImage: str = dI["dockerImage"]
class vncApp:
        def __init__(self, info: str) -> None:
            parsed = json.loads(info)
            self.name: str = parsed["name"]
            self.displayName: str = parsed["displayName"]
            self.name: str = parsed["name"]
            self.color: str = parsed["color"]
            self.icons: dict = parsed["icons"]
            self.fileExtensions: list[str] = parsed["fileExtensions"]
            self.isInternal: bool = parsed["isInternal"]
            self.dockerVersion: DockerInfo = parsed["dockerVersion"]
            self.opsiVersion = parsed["opsiVersion"]
            self.appSourceName: str = parsed["appSourceName"]
            self.appSourceDisplayName: str = parsed["appSourceDisplayName"]

class vncContainer:
    def __init__(self) -> None:
        pass