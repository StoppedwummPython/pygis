# Documentation
## User
```python
        userName: str
        firstName: str
        lastName: str
        displayName: str
        mail: str
        mailAliases: list[str]
        role: str
        roleGroups: list
        creationTime: datetime
        dn: str
        profilePath: str
        uid: int
        gid: int
        sid: str
        primaryGroupID: int
        isStudent: bool
        isEmployee: bool
        isTeacher: bool
        isAdmin: bool
```

## VNC
### VNC Container
```python
        s.id: str
        s.creationTime: str 
        s.appName: str
        s.displayName: str
        s.color: str
        s.icons: dict
        s.dockerImage: str
        s.isInternal: bool
        s.accessors: dict[s.accessor]
        s.status: str
        s.lastStatusUpdate: str
        s.nodeName: str
        s.connectInfo: dict[s.connectInfoClass]
        s.dockerContainerName: str
        s.dockerContainerIp: str
        s.dockerContainerVncPort: int
        s.ownerUserName: str
```

### VNC App
```python
            self.name: str
            self.displayName: str
            self.name: str
            self.color: str
            self.icons: dict
            self.fileExtensions: list[str]
            self.isInternal: bool
            self.dockerVersion: DockerInfo
            self.opsiVersion
            self.appSourceName: str
            self.appSourceDisplayName: str
```