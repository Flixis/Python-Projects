import json


with open('Python-Projects\JSON\latestrelease.json') as f:
    data = json.load(f)

print(json.dumps(data,indent=2))

for item in data['releases']:
    releasev = item['stable']

print("V%s" % releasev)