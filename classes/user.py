import json
import datetime
from classes.permissions import *
class user:
        userName = ""
        firstName = ""
        lastName = ""
        displayName = ""
        mail = ""
        mailAliases = []
        role = ""
        roleGroups = []
        creationTime = ""
        dn = ""
        profilePath = ""
        uid = 0
        gid = 0
        sid = ""
        primaryGroupID = 0
        isStudent = False
        isEmployee = False
        isTeacher = False
        isAdmin = False
        def __init__(s, userInfo: dict | None = None, onlyUser: bool = False) -> None:
            if userInfo == None:
                return
            
            p: dict
            if onlyUser:
                 p = userInfo
            else:
                 p = userInfo["entry"]
            s.creationTime: datetime.datetime = datetime.datetime.fromisoformat(p["creationTime"])
            s.displayName = p["displayName"]
            s.userName = p["userName"]
            s.dn = p["dn"]
            s.firstName = p["firstName"]
            s.gid = p["gid"]
            s.isAdmin = p["isAdmin"]
            s.isEmployee = p["isEmployee"]
            s.isStudent = p["isStudent"]
            s.isTeacher = p["isTeacher"]
            s.lastName = p["lastName"]
            s.mail = p["mail"]
            s.mailAliases = p["mailAliases"]
            s.primaryGroupID = p["primaryGroupID"]
            s.profilePath = p["profilePath"]
            s.role = p["role"]
            s.roleGroups = p["roleGroups"]
            s.sid = p["sid"]
            s.uid = p["uid"]
            perms: dict[str: Permission] = {}

            if onlyUser:
                 return
            for name, action in userInfo["availableActions"].items():
                perms[name] = Permission(action, name)
            s.avaibleActions = perms