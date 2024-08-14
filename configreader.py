import json

def readConfig(filepath: str = "config.json"):
    content = ""
    with open(filepath, "r") as f:
        content = json.loads(f.read())
    return content
    