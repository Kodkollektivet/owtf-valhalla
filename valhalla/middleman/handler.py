"""
# >>> from valhalla.dockerutils import OwtfContainer
# >>> from valhalla.middleman.handler import send_for_execution
# >>> oc = OwtfContainer('valhalla/containers/testcontainer')
# >>> oc.build_image()
# >>> oc.build_container()
# >>> oc.start()
# >>> oc.is_running
# True
# >>> send_for_execution(oc, {'command': 'ping -c 1 scanme.nmap.org'})
# {...}
"""

import requests
import json
import time
from datetime import datetime

from valhalla.dockerutils import OwtfContainer


def send_for_execution(image: OwtfContainer, cmd) -> dict:
    """Sends the command to the container
    and return result in a dict.
    """
    cmd_org = cmd
    cmd = json.dumps(cmd)

    start_time = datetime.now().strftime('%d-%m-%y %H:%M:%S')
    address = 'http://' + image.ip_address + ':' + str(image.port) + '/'

    requests.post(address + 'run', data=cmd)

    result_request = requests.get(address + 'result')

    while result_request.json()['status'] != 0:
        result_request = requests.get(address + 'result')
        print(result_request.text)
        time.sleep(2)

    return {
        'start_time': start_time,
        'stop_time': datetime.now().strftime('%d-%m-%y %H:%M:%S'),
        'result': result_request.json()['response'],
        'command': cmd_org,
        'image': image.image
    }

