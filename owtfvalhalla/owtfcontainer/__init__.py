"""
This module takes care of all the Docker stuff.

When the application starts we will iterate over all of the
containers that lives in 'owtfvalhalla/containers' and build
OwtfContainer objects.
The OwtfContainer object can interact with image/container,
give IP address of running container, give all the information
that is relevant to a container/image.
"""

__author__ = 'owtf-valhalla'

from owtfcontainerIter2 import OwtfContainer
from handler import owtf_containers_located_in_container_folder, locate_owtf_containers



