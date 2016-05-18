"""
This is iteration 2 of the OwtfContainer.
This one is the one that have been refactored and
the one we should build from
"""

import os
import pprint
import json
import logging
from core.exceptions.DockerImageException import DockerImageException
from core.exceptions.DockerContainerException import DockerContainerException
from . import dclient as dc

# List with ports that can be assigned to container
_available_ports = [i for i in range(6000, 6100, 1)]  # 100 containers

log = logging.getLogger(__name__)


class OwtfContainer(object):
    """OwtfContainer matches images and containers in the core/cotainers dir."""

    def __init__(self, owtf_image_path):

        self.image = None
        self.image_id = None  # The id of the build image
        self.image_name = None  # The name if the image
        self.image_version = None  # The image version
        self.image_path = os.path.abspath(owtf_image_path)  # Path to image. Dcokerfile/config.json lives here

        self.container_id = None  # Build container id
        self.container_name = None  # Build container name
        self.container_tag = None  # The build container tag (container_name + container_version)

        self.config = None  # The config.json file in loaded in here
        self.ip_address = None  # Container ip address
        self.port = None  # Forwarding port in the container

        self.is_image_built = False
        self.is_container_built = False
        self.is_valid = False
        self.is_running = False

        self.log = ''  # This string will contain log output.
        self.results = []

        self._validate_config_image_and_container()  # Start the validation

    def _validate_config_image_and_container(self):
        """Internal validator
        Validate that files and folders are in place.
        Check if image/container is built/running.
        """
        # Check required files and folders
        log.debug('Validating: ' + self.image_path)
        if not os.path.isdir(self.image_path):
            self.is_valid = False
            log.debug('Can\'t find container dir! NOT VALID!')
            return

        elif not os.path.isfile(os.path.join(self.image_path, 'config.json')):
            self.is_valid = False
            log.debug('Can\'t find config.json! NOT VALID!')
            return

        elif not os.path.isfile(os.path.join(self.image_path, 'Dockerfile')):
            self.is_valid = False
            log.debug('Can\'t find Dockerfile! NOT VALID!')
            return

        else:
            self.is_valid = True
            log.debug('Container files and folder are in place.')

        # Validate config.json and read it
        log.debug('Inspecting config.json file.')
        try:
            with open(os.path.join(self.image_path, 'config.json')) as configfile:
                self.config = json.load(configfile)
                self.image_name = self.config['title']
                self.image_version = self.config['version']
                self.image = self.image_name.lower() + ':' + self.image_version  # Docker wants this
                log.debug('Inspection OK.')

        except ValueError as e:
            self.is_valid = False
            # a bit more informative error, tells where the error was in JSON
            log.debug('config.json is not valid!\n\t' + e.message)
            return

        # Check if image is built
        for image in dc.cli.images():
            if self.image == image['RepoTags'][0]:
                self.is_image_built = True
                self.image_id = image['Id']
                log.debug('Image is built.')

        # Check if container is built
        for container in dc.cli.containers(all=True):
            if self.image_id == container['ImageID']:
                log.debug('Container is built.')
                if dc.is_linux:
                    self.port = 5000
                else:
                    try:
                        self.port = container['Ports'][0]['PublicPort']  # Assign the port.
                        _available_ports.remove(self.port)  # Remove port from _available ports.

                    except Exception as e:
                        log.debug(e)


                self.is_container_built = True
                self.container_id = container['Id']
                self.container_name = self.inspect().get('Name')

        # Check if container is running
        for container in dc.cli.containers():
            if self.container_id == container['Id']:
                log.debug('Container is running.')
                self.container_name = container['Names'][0]
                if dc.is_linux:
                    self.ip_address = container['NetworkSettings']['Networks']['bridge']['IPAddress']
                else:
                    self.ip_address = '192.168.99.100'
                self.is_running = True

        log.debug('Validation and inspection ends. Container looks OK!')

    def build_image(self):
        """Build image.
        If image is valid, build it.
        After image is built, assign image_id to obj.
        Validate that image exists in docker land.
        """
        if self.is_valid and not self.is_image_built:

            log.debug(self.image + ' building image...')
            for build_log in dc.cli.build(path=self.image_path, rm=True, tag=self.image):
                log.debug(build_log.replace('\n', ''))

            self.image_id = [i for i in dc.cli.images() if self.image in i['RepoTags']][0].get('Id')

            if self.image_id in [i['Id'] for i in dc.cli.images()] \
                    and self.image in [i['RepoTags'][0] for i in dc.cli.images()]:
                self.is_image_built = True

            else:
                log.error('Could not find the built image!')
                raise DockerImageException('Failed to build image!')

    def remove_image(self):
        """Remove image.
        Validate that image have been removed in docker land.
        """
        if self.is_image_built:
            log.debug(self.image + 'removing image...')
            dc.cli.remove_image(image=self.image, force=True)
            if self.image_id not in [i['Id'] for i in dc.cli.images()]:
                self.is_image_built = False
            else:
                log.error('Image was not removed!')
                raise DockerImageException('Failed to remove image!')

    # Container related methods
    def build_container(self):
        """Build container.
        Check what OS application is running on.
        Set port and ip depending on OS.
        Get container id and name.
        Validate that container exists in docker land.
        """
        if self.is_valid and self.is_image_built and not self.is_container_built:
            log.debug(self.image + 'building container...')

            if dc.is_linux:
                self.port = 5000
                container = dc.cli.create_container(image=self.image, command='app.py')

            else:
                self.port = _available_ports.pop(0)
                container = dc.cli.create_container(
                    image=self.image,
                    command='app.py',
                    ports=[5000],
                    host_config=dc.cli.create_host_config(
                        port_bindings={
                            5000: [
                                ('0.0.0.0', self.port)
                            ]
                        }
                    )
                )
            self.container_id = container.get('Id')
            self.container_name = self.inspect().get('Name')

            if self.container_id in [i['Id'] for i in dc.cli.containers(all=True)]:
                self.is_container_built = True
            else:
                log.error('Container could not be found.')
                raise DockerContainerException('Container could not be found in docker containers!')

    def remove_container(self):
        """Remove container.
        Check what OS application is running on.
        Depending on OS remove port and put it back in port list.
        Validate that container have been removed from docker land.
        """
        if self.is_container_built:
            self.stop()
            log.debug(self.image + 'removing container...')
            if not dc.is_linux:
                self.port = None
                _available_ports.append(self.port)

            dc.cli.remove_container(container=self.container_id, force=True)

            if self.container_id not in [i['Id'] for i in dc.cli.containers(all=True)]:
                self.container_id = None
                self.container_name = None
                self.is_container_built = False

            else:
                log.error('Container was not removed.')
                raise DockerContainerException('Container is still found in docker containers!')

    def start(self):
        """Start container.
        Start container.
        Validate that container is running in docker land.
        """
        if self.is_valid and self.is_image_built and self.is_container_built and not self.is_running:
            log.debug(self.image + ' starting container...')
            dc.cli.start(container=self.container_id)

            if self.container_id in [i['Id'] for i in dc.cli.containers()]:
                info = dc.cli.inspect_container(container=self.container_id)
                self.is_running = True
                if dc.is_linux:
                    self.ip_address = info['NetworkSettings']['Networks']['bridge']['IPAddress']
                else:
                    self.ip_address = '192.168.99.100'
            else:
                log.error('Container could not be found in started docker containers')
                raise DockerContainerException('Container could not be found in started docker containers')

    def stop(self):
        """Stop running container if running.
        Validate that container is not running in docker land.
        """
        if self.is_running:
            log.debug(self.image + ' stopping container...')
            dc.cli.stop(container=self.container_id)
            if self.container_id not in [i['Id'] for i in dc.cli.containers()]:
                self.is_running = False
            else:
                log.error('Container could still be found in started docker containers')
                raise DockerContainerException('Container could still be found in started docker containers')

    def inspect(self):
        """Inspec running container.
        :return json obj
        """
        return dc.cli.inspect_container(container=self.container_id)

    def get_available_commands(self):
        """Returns the part of config.json that contains available commands.
        :return json obj
        """
        return json.dumps(self.config.get('commands'))

    def __eq__(self, other):
        """obj1 == obj2"""
        this = str(self.image_id) + str(self.container_id) + str(self.container_name)
        other = str(other.image_id) + str(other.container_id) + str(other.container_name)
        return this == other

    def __repr__(self):
        """Gives a nice json-like output for debug."""
        return pprint.pformat(self.__dict__, indent=4)

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __str__(self):
        return 'OwtfContainer({}) based on image: ({},{})'.format(
            self.container_name,
            self.image_name,
            self.image_version
        )

