import requests.cookies
import json
from classes.user import *
from classes.course import *
from classes.vnc import *
from functions.requester import *
from webdav4.client import Client
import sys


class magisSession:
    isLoggedIn = False
    def __init__(self, frontend: str, backend: str, webdav: str) -> None:
        self.fr = frontend
        self.bck = backend
        self.wbd = webdav
    
    def login(self, username: str, password: str):
        loginrq = CreateRequest(getRoute(self.bck, "/api/web/auth/login"), json.dumps({
            "UserNameOrMail": username,
            "Password": password
        }))
        self.cookies = loginrq.cookies
        u = user(loginrq.text)
        self.loggedIn = u
        self.isLoggedIn = True
        self.webdavClient = Client(self.wbd, auth=(username, password))
        return u
    
    def getUsers(self):
        ur = CreateRequest(getRoute(self.bck, "/api/web/users"), cookies=self.cookies, method="GET")
        parsed = ur.json()
        users: list[user] = []
        for entry in parsed["entries"]:
            urev = json.dumps(entry["entry"])
            u = user(urev)
            users.append(u)
        return users
    
    def getCourses(self):
        cr = CreateRequest(getRoute(self.bck, "/api/web/courses"), cookies=self.cookies, method="GET")
        pcr = cr.json()
        courses: list[course] = []
        for entry in pcr["entries"]:
            courses.append(course(json.dumps(entry["entry"])))
        return courses
    
    def getApps(self):
        ar = CreateRequest(getRoute(self.bck, "/api/web/apps"), cookies=self.cookies, method="GET")
        parsed = ar.json()
        apps: list[vncApp] = []
        for entry in parsed["entries"]:
            reverted = json.dumps(entry["entry"])
            app = vncApp(reverted)
            apps.append(app)
        return apps
    
    def getContainers(self):
        cr = CreateRequest(getRoute(self.bck, "/api/web/vnc-containers"), cookies=self.cookies, method="GET")
        parsed = cr.json()
        containers = []
        for entry in parsed["entries"]:
            containers.append(vncContainer(json.dumps(entry["entry"])))
        return containers
            
    def logOut(self):
        if self.isLoggedIn:
            res = CreateRequest(getRoute(self.bck, "/api/web/auth/logout"), cookies=self.cookies)
            if res.ok:
                self.isLoggedIn = False
                self.loggedIn = user()
                self.cookies = requests.cookies.RequestsCookieJar()
            else:
                raise Exception(res.text)

if __name__ == "__main__":
    from fernet import Fernet
    #import configreader
    #cfg = configreader.readConfig()
    #crypt = Fernet(cfg["encKey"].encode())
    pwd = sys.argv[1]
    username = sys.argv[2]
    frontend = sys.argv[3]
    backend = sys.argv[4]
    webdav = sys.argv[5]
    

    s = magisSession(frontend, backend, webdav)
    s.login(username, pwd)
    s.getUsers()
    s.logOut()



    
