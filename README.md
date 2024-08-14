
# Pygis
An Magis API written with and for python


## Installation

Obtain the files to the API, then move it to your project

```python
import pygis
```
    
## Functions
### Login
Log into the session with
```python
import pygis
ms = pygis.magisSession(frontend, backend, webdav)
ms.login(username, pwd)
```

`ms.login` will return an `user` object.

### Obtain Infos
You can obtain your courses with `.getCourses()`.

`.getApps` returns all Apps.

`.getUsers` returns all Users.