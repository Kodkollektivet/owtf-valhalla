import os
import fnmatch

from owtfvalhalla.owtfcontainer import *

containers = []


def locate_owtf_containers():
    """Locates the containers that lives inside of the container folder.
    The containers list the filled up with OwtfContainer objects.
    """
    global containers
    #matches = []
    containers = []
    # print(os.path.abspath('.'))
    for root, dirnames, filenames in os.walk('owtfvalhalla/containers'):
        # print(root)
        # print(dirnames)
        # print(filenames)
        for filename in fnmatch.filter(filenames, 'config.json'):
            if 'Dockerfile' and 'config.json' in filenames:
                containers.append(OwtfContainer(root))
                #matches.append(root)
    #return matches

locate_owtf_containers()
