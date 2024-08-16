import sys
from everything import *
if __name__ == "__main__":
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
    s.logOut()