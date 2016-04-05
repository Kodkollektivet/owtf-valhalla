import requests
import json
import time

def send_for_execution(ipaddress, cmd):
    cmd = json.dumps(cmd)
    run_request = requests.post('http://'+ipaddress+'/run', data=cmd)

    result_request = requests.get('http://'+ipaddress+'/result')
    
    while result_request.json()['status'] != 0:
        result_request = requests.get('http://'+ipaddress+'/result')
        time.sleep(2)
        
    print(result_request.json())


if __name__ == '__main__':
    a = send_for_execution('172.17.0.2:5000', {'command':'ping -c 2 idg.se'})
    
    
