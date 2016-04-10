"""
This is iteration 2 of the OwtfContainer.
This one is the one that have been refactored and
the one we should build from
"""

import os
import pprint
import json

from dclient import *


class OwtfContainer(object):
    """OwtfContainer matches images and containers in the owtfvalhalla/cotainers dir."""

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

        self.is_image_build = False
        self.is_container_build = False
        self.is_valid = False
        self.is_running = False

        self.log = ''  # This string will contain log output.
        self.results = []

        self._validate_config_image_and_container()  # Start the validation

    def _validate_config_image_and_container(self):
        """Internal validator"""
        # Check required files and folders
        if not os.path.isdir(self.image_path):
            self.is_valid = False
            print('Cant find containers dir...')
            # TODO: Add log message
            return

        elif not os.path.isfile(os.path.join(self.image_path, 'config.json')):
            self.is_valid = False
            print('Cant find config.json...')
            # TODO: Add log message
            return

        elif not os.path.isfile(os.path.join(self.image_path, 'Dockerfile')):
            self.is_valid = False
            print('Cant find Dockerfile...')
            # TODO: Add log message
            return

        else:
            self.is_valid = True
            # TODO: Add log message

        # Validate config.json and read it
        try:
            with open(os.path.join(self.image_path, 'config.json')) as configfile:
                self.config = json.load(configfile)
                self.image_name = self.config['title']
                self.image_version = self.config['version']
                self.image = self.image_name.lower() + ':' + self.image_version  # Docker wants this
                # TODO: Add log message

        except ValueError as e:
            self.is_valid = False
            # TODO: Add log message
            return

        # Check if image is build
        for image in cli.images():
            if self.image == image['RepoTags'][0]:
                self.is_image_build = True
                self.image_id = image['Id']

        # Check if container is build
        for container in cli.containers(all=True):
            if self.image_id == container['ImageID']:
                self.is_container_build = True
                self.container_id = container['Id']
                self.container_name = self.inspect().get('Name')

        # Check if container is running
        for container in cli.containers():
            if self.container_id == container['Id']:
                self.container_name = container['Names'][0]
                self.ip_address = container['NetworkSettings']['Networks']['bridge']['IPAddress']
                self.is_running = True
        print('The OwtfContainer is valid!')

    def build_image(self):
        """Build image."""
        if self.is_valid and not self.is_image_build:
            print('Building image...')
            for log in cli.build(path=self.image_path, rm=True, tag=self.image):
                print(log,)
            self.is_image_build = True
            self.image_id = (i for i in cli.images() if i['RepoTags'][0] == self.image).next().get('Id')

    def remove_image(self):
        """Remove image."""
        if self.is_image_build:
            print('Removing image...')
            cli.remove_image(image=self.image, force=True)
            self.is_image_build = False

    # Container related methods
    def build_container(self):
        """Build container."""
        if self.is_valid and self.is_image_build and not self.is_container_build:
            print('Building container...')
            container = cli.create_container(image=self.image, command='app.py')
            self.is_container_build = True
            self.container_id = container.get('Id')
            self.container_name = self.inspect().get('Name')

    def remove_container(self):
        """Remove container."""
        if self.is_container_build:
            print('Removing container...')
            cli.remove_container(container=self.container_id, force=True)
            self.is_container_build = False

    def start(self):
        """Start container."""
        if self.is_valid and self.is_image_build and self.is_container_build and not self.is_running:
            print('Starting container...')
            cli.start(container=self.container_id)
            info = cli.inspect_container(container=self.container_id)
            self.is_running = True
            self.ip_address = info['NetworkSettings']['Networks']['bridge']['IPAddress']

    def stop(self):
        """Stop running container if running."""
        if self.is_running:
            print('Stopping container...')
            cli.stop(container=self.container_id)
            self.is_running = False

    def inspect(self):
        """Inspec running container.
        :return json obj
        """
        return cli.inspect_container(container=self.container_id)

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

# For manual testing
# if __name__ == '__main__':
#     oc = OwtfContainer('containers/testcontainer')
#     pprint.pprint(oc)

