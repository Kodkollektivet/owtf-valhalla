import os
import fnmatch
import json
from pprint import pprint

from .owtfcontainer import OwtfContainer

_containers = []
commands = []

def locate_owtf_containers(location='containers'):
    """Locates the containers that lives inside of the container folder.
    The containers list the filled up with OwtfContainer objects.

    location is only used for testing.
    """
    for root, dirnames, filenames in os.walk(location):
        for filename in fnmatch.filter(filenames, 'config.json'):
            if 'Dockerfile' and 'config.json' in filenames:
                _containers.append(OwtfContainer(root))


def aggregate_owtf_codes():
    """Get all commands available.
    Iterates over all of the containers and
    assembles the commands from each of the
    container.
    """
    commandDict = {}
    for container in _containers:
        for command in container.config['commands']:
            code = command['code']
            command['image'] = container.image
<<<<<<< c234f5bb9510534bea38203ff457e7a57b123be3
            commandDict.setdefault(code, []).append(command)
    for key, value in commandDict.iteritems():
        codeDict = {'code': key, 'commands': value}
        commands.append(codeDict)
=======
            commands.append(command)

>>>>>>> Restructured command list API response to be just a list of command objects instead of an object itself where every command is a field with the code as a name. The reason for this being that the React component in the client should be able to iterate it as an array of objects

locate_owtf_containers()
aggregate_owtf_codes()


def get_owtf_c(image=None, image_id=None, container_id=None):
    """This is the facade to the outside.
    If get_owtf_c() with no arguments is called, returns all the containers
    If get_owtf_c(image=<IMAGE>), return that container
    If get_owtf_c(image=<IMAGE_ID>) if image is build, return that container
    If get_owtf_c(image=<CONTAINER_ID>) if container is buld, return that container

    Only one or no argument can be passed.

    Returns a tuple (bool, obj)
    bool = status
    obj = object
    """

    if image and image_id and container_id is not None:
        return False, ValueError("All params cant be set. Choose one of them of none.")

    elif image is not None:
        for img in _containers:
            if img.image == image:
                return True, img
        return False, None

    elif image_id is not None:
        for image in _containers:
            if image_id == image.image_id:
                return True, image
        return False, None

    elif container_id is not None:
        for container in _containers:
            if container_id == container.container_id:
                return True, container
        return False, None

    else:
        return True, _containers
