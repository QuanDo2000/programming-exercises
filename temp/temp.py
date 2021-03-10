import json

with open('./temp.txt', 'r') as f:
    raw_data = json.load(f)

data = json.loads(raw_data['data'])
for key, value in data.items():
    print('\n{}: {}'.format(key, value))
