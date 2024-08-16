import json
from functions.requester import *
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
        def startApp(self, backend: str, cookies: requests.cookies.RequestsCookieJar):
            r = createRequest(getRoute(backend, "/api/web/apps/" + self.name), cookies=cookies)
            name = r.text
            cr = createRequest(getRoute(backend, "/api/web/vnc-containers/" + name), cookies=cookies, method="GET")
            ob = vncContainer(json.dumps(cr.text))
            return ob

class vncContainer:
    class accessor:
         def __init__(self, ainfo: dict) -> None:
              self.user: str = ainfo["user"]
              self.type: str = ainfo["type"]
              self.accessLevel: str = ainfo["accessLevel"]
    class connectInfoClass:
         def __init__(s, info: dict) -> None:
              s.nodeIP: str = info["nodeIP"]
              s.vncHost: str = info["vncHost"]
              s.vncPort: int = info["vncPort"]
              s.websockifyPort: int = info["websockifyPort"]
              s.password: str = info["password"]
              s.readOnlyPassword: str = info["readOnlyPassword"]


    def __init__(s, info: str) -> None:
        p = json.loads(info)
        s.id: str = p["id"]
        s.creationTime: str = p["creationTime"]
        s.appName: str = p["appName"]
        s.displayName: str = p["displayName"]
        s.color: str = p["color"]
        s.icons: dict = p["icons"]
        s.dockerImage: str = p["dockerImage"]
        s.isInternal: bool = p["isInternal"]
        s.accessors: dict[s.accessor] = p["accessors"]
        s.status: str = p["status"]
        s.lastStatusUpdate: str = p["lastStatusUpdate"]
        s.nodeName: str = p["nodeName"]
        s.connectInfo: dict[s.connectInfoClass] = s.connectInfoClass(p["connectInfo"])
        s.dockerContainerName: str = p["dockerContainerName"]
        s.dockerContainerIp: str = p["dockerContainerIp"]
        s.dockerContainerVncPort: int = p["dockerContainerVncPort"]
        s.ownerUserName: str = p["ownerUserName"]