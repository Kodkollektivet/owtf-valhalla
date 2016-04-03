import os
import fnmatch

from owtfcontainerIter2 import *

owtf_containers_located_in_container_folder = []


def locate_owtf_containers():
    """Locates the containers that lives inside of the container folder.
    The containers list the filled up with OwtfContainer objects.
    """
    print('In here')
    global owtf_containers_located_in_container_folder
    print(os.path.abspath('.'))
    for root, dirnames, filenames in os.walk('containers'):

        for filename in fnmatch.filter(filenames, 'config.json'):
            if 'Dockerfile' and 'config.json' in filenames:
                owtf_containers_located_in_container_folder.append(OwtfContainer(root))

locate_owtf_containers()

