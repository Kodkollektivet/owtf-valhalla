import json

x=[]

p = open('config.json')
u = p.read()
config = json.loads(u)

#Function that checks if there is duplicated codes (Ex. OTG-INFO-004) in the configuration file
def checkDuplicateCodes():
    for i in config['commands']:
        x.append(i['code'])

    if len(x) != len(set(x)):
        print('There are duplicate codes')

    else:
        print('There are no duplicate codes')

#Function that checks if there is commands with keys that have no values
#in the configuration file
def checkEmptyValues():
    flag = True
    for i in config['commands']:
        for key, value in i.iteritems():
            if value=='?':
                print("The The Key "+str(key)+" from the command "+str(i['command'])+" has no value")
                flag = False
    if flag:
        print("There are no empty key-values")



checkEmptyValues()
checkDuplicateCodes()





