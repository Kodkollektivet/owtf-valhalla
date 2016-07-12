import os
import fnmatch
import json
from pprint import pprint

from .owtfcontainer import OwtfContainer
from valhalla.django.settings.settings import CONTAINER_DIR

_containers = []
_objectives_and_commands = []


def _locate_valhalla_containers(location=CONTAINER_DIR):
    """Locates the Valhalla containers that lives inside the
    container folder and adds them to the _containers list.

    location paramater is only used for testing.
    """
    _containers.clear()
    for root, dirnames, filenames in os.walk(location):
        for filename in fnmatch.filter(filenames, 'config.json'):
            if 'Dockerfile' and 'config.json' in filenames:
                _containers.append(OwtfContainer(root))


def _aggregate_owtf_codes():
    """Get all commands available.
    Iterates over all of the containers and
    assembles the commands from each of the
    container.
    """
    _objectives_and_commands.clear()
    command_dict = {}
    for container in _containers:
        for command in container.config['commands']:
            code = command['code']
            command['image'] = container.image
            command_dict.setdefault(code, []).append(command)
    for key, value in command_dict.items():
        code_dict = {'code': key, 'commands': value}
        _objectives_and_commands.append(code_dict)


def get_objectives_and_commands() -> list:
    """Returns a list of dicts, containing OWASP pentesting objectives along
    with a list of commands related to objective.
    """
    return _objectives_and_commands


def get_valhalla_container(image=None, image_id=None, container_id=None) -> tuple:
    """This is the facade to the outside.
    If get_valhalla_container() with no arguments is called, returns all the containers
    If get_valhalla_container(image=<IMAGE>), return that container
    If get_valhalla_container(image=<IMAGE_ID>) if image is build, return that container
    If get_valhalla_container(image=<CONTAINER_ID>) if container is buld, return that container

    Only one or no argument can be passed.

    Returns a tuple (bool, obj)
    bool = status
    obj = object

    >>> from valhalla.dockerutils import OwtfContainer, get_valhalla_container
    >>> status, container = get_valhalla_container(image='owtfvalhallatestcontainer:0.1')
    >>> status
    True
    >>> isinstance(container, OwtfContainer)
    True
    >>> status, container = get_valhalla_container(image='doesnotexists:0.1')
    >>> status
    False
    >>> container  # is None
    >>> status, containers = get_valhalla_container()
    >>> status
    True
    >>> isinstance(containers, list)  # Contains all the Valhalla containers
    True
    >>>
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

# Find containers, objectives and commands.
_locate_valhalla_containers()
_aggregate_owtf_codes()
