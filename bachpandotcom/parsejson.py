import json

# read file
with open('bachpan.json', 'r') as myfile:
    data = myfile.read()

# parse file
data = json.loads(data)

names = set()
for x in data:
    names.update(x['data'])

# print(names)

with open('bachpan.txt', 'w') as myfile:
    for name in names:
        data = myfile.write(name + "\n")
