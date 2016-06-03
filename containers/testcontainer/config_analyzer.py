import json

x=[]

p = open('config.json')
u = p.read()
config = json.loads(u)
file = open('config_analyzer_log.txt', 'w+')

#Function that checks if there is duplicated codes (Ex. OTG-INFO-004) in the configuration file
def checkDuplicateCodes():
    file.write("Checking duplicate codes...\n")
    for i in config['commands']:
        x.append(i['code'])

    if len(x) != len(set(x)):
        print('There are duplicate codes')
        file.write('There are duplicate codes in the config file\n')
    else:
        print('There are no duplicate codes')
        file.write('There are duplicate codes in the config file\n')

#Function that checks if there is commands with keys that have no values
#in the configuration file
def checkEmptyValues():
    file.write("Checking empty key-values...\n")
    for i in config['commands']:
        for key, value in i.iteritems():
            print(key, value)
            if not value:
                file.write("Command: "+str(i['code'])+" The Key "+str(key)+" has no value\n")
                print("no value in the key")


checkEmptyValues()
checkDuplicateCodes()





