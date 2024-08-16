import urllib.parse
import requests
import requests.cookies

def getRoute(domain: str, route: str) -> str:
    return urllib.parse.urljoin(domain, route)

def createRequest(route: str, data: str | None = None, cookies: requests.cookies.RequestsCookieJar | None = None, method: str = "POST"):
    rq = requests.request(url=route, data=data, headers={
        "X-Requested-With": "Pygis",
        "Content-Type": "application/json"
    }, cookies=cookies, method=method)
    if not rq.ok:
        raise ConnectionError(rq.status_code, rq.text)
    return rq