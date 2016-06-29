import os
import fnmatch

from .owtfcontainer import OwtfContainer

_containers = []


def locate_owtf_containers(location='containers'):
    """Locates the containers that lives inside of the container folder.
    The containers list the filled up with OwtfContainer objects.

    location is only used for testing.
    """
    for root, dirnames, filenames in os.walk(location):
        for filename in fnmatch.filter(filenames, 'config.json'):
            if 'Dockerfile' and 'config.json' in filenames:
                _containers.append(OwtfContainer(root))

locate_owtf_containers()


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




