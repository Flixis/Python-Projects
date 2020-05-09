import urllib.request, json 

with urllib.request.urlopen("http://welldonelasagna.com/latestrelease.json") as url:
    data = json.loads(url.read().decode())
    