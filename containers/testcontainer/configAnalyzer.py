__author__ = 'oerlex'
import json

x=[]

p = open('config.json')
u = p.read()
config = json.loads(u)

for i in config['commands']:
    x.append(i['code'])

if len(x) != len(set(x)):
    print('There are duplicate codes')
else:
    print('There are no duplicate codes')
