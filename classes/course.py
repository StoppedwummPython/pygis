import json
class course:
        def __init__(se, infoString: str) -> None:
            parsed = json.loads(infoString)
            se.name: str = parsed["name"]
            se.mail: str = parsed["mail"]
            se.members: list[str] = parsed["members"]
            se.sid: str = parsed["sid"]
            se.gid: int = parsed["gid"]
            se.dn: str = parsed["dn"]
            se.creationTime: str = parsed["creationTime"]
            se.displayName: str = parsed["displayName"]
            se.lessonStarted: bool = parsed["lessonStarted"]
            return