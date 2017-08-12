import json

str = None
with open('residential.json') as f:
    str = f.read();

j = json.loads(str)
pass