"""Module for interacting with containers.

Send commands to containers.

>>> from valhalla.dockerutils import OwtfContainer
>>> from valhalla.middleman.handler import send_for_execution
>>> import time
>>> oc = OwtfContainer('valhalla/containers/testcontainer')
>>> oc.build_image()
>>> time.sleep(2)  # Only here for doctest to pass
>>> oc.build_container()
>>> time.sleep(2)  # Only here for doctest to pass
>>> oc.start()
>>> time.sleep(2)  # Only here for doctest to pass
>>> oc.is_running
True
>>> send_for_execution(oc, {'command': 'ping -c 1 scanme.nmap.org'})
{...}
"""
from .handler import send_for_execution