import requests
import json
import time


def send_for_execution(ipaddress, cmd):
    """Sends the command to the container and asks for result.
    """

    remote_host = 'http://'+ipaddress+':5000/run'
    requests.post(remote_host, data=cmd)

    result_request = requests.get('http://'+ipaddress+'/result')

    while result_request.json()['status'] != 0:
        result_request = requests.get('http://'+ipaddress+'/result')
        time.sleep(2)

    return result_request.json()


if __name__ == '__main__':
    a = send_for_execution('172.17.0.2', {'command': 'ping -c 2', 'target': 'idg.se'})


