import requests
import json
import time


def send_for_execution(ipaddress, cmd):
    """Sends the command to the container and asks for result.
    """
    cmd = json.dumps(cmd)
    requests.post('http://'+ipaddress+':5000/run', data=cmd)

    result_request = requests.get('http://'+ipaddress+':5000/result')

    while result_request.json()['status'] != 0:
        result_request = requests.get('http://'+ipaddress+':5000/result')
        print(result_request.text)
        time.sleep(2)

    return result_request.json()


if __name__ == '__main__':
    a = send_for_execution('172.17.0.3', json.dumps({'command': 'ping -c 2 idg.se'}))


