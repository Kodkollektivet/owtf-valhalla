import requests
import json
import time


def send_for_execution(ipaddress, port, cmd):
    """Sends the command to the container and asks for result.
    """
    cmd = json.dumps(cmd)

    address = 'http://' + ipaddress + ':' + str(port) + '/'

    requests.post(address + 'run', data=cmd)

    result_request = requests.get(address + 'result')

    while result_request.json()['status'] != 0:
        result_request = requests.get(address + 'result')
        print(result_request.text)
        time.sleep(2)

    return result_request.json()

