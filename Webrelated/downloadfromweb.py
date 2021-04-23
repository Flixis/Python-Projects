import requests



url = 'http://welldonelasagna.com/latestrelease.xml'
r = requests.get(url, allow_redirects=True)

with open('Python-Projects\Download_from_internet\Release.xml', 'wb') as f:
    f.write(r.content)