import unittest

from core.dockerutils import OwtfContainer
from core.dockerutils.dclient import *


class OwtfContainerTest(unittest.TestCase):
    """Integration tests for the OwtfContainer object.
    This tests the basic functions of the OwtfContainer object:
    Build image
    Build container
    Start
    Stop
    Remove container
    Remove image

    The test will clean up the container and image of the testcontainer.
    The test requires internet connection and can vary in time depending on
    bandwith.
    """

    def setUp(self):
        """Remove all containers and images before """
        self.container_location = 'containers/testcontainer'

    def test_01_stop_remove_image_and_container(self):
        oc = OwtfContainer(self.container_location)

        oc.stop()
        self.assertFalse(oc.is_running)

        if oc.is_container_build:
            oc.remove_container()
            self.assertFalse(oc.is_container_build)

        if oc.is_image_build:
            oc.remove_image()
            self.assertFalse(oc.is_image_build)

        self.assertFalse(oc.is_image_build)
        self.assertFalse(oc.is_container_build)
        self.assertFalse(oc.image_id in [i['Id'] for i in cli.images()])
        self.assertFalse(oc.container_id in [i['Id'] for i in cli.containers(all=True)])

    def test_02_not_valid_location(self):
        oc = OwtfContainer(self.container_location + 's')  # Wrong location
        self.assertFalse(oc.is_valid)

    def test_03_validate_location(self):
        oc = OwtfContainer(self.container_location)
        self.assertTrue(oc.is_valid)

    def test_04_build_image(self):
        oc = OwtfContainer(self.container_location)
        self.assertTrue(oc.is_valid)
        oc.build_image()
        self.assertTrue(oc.is_image_build)
        self.assertTrue(oc.image_id in [i['Id'] for i in cli.images()])

    def test_05_build_container(self):
        oc = OwtfContainer(self.container_location)
        self.assertTrue(oc.is_image_build)
        self.assertFalse(oc.is_container_build)
        oc.build_container()
        self.assertTrue(oc.is_container_build)
        self.assertTrue(oc.container_id in [i['Id'] for i in cli.containers(all=True)])

    def test_06_start_contianer(self):
        oc = OwtfContainer(self.container_location)
        self.assertTrue(oc.is_image_build)
        self.assertTrue(oc.is_container_build)
        oc.start()
        self.assertTrue(oc.is_running)
        self.assertTrue(oc.container_id in [i['Id'] for i in cli.containers()])

    def test_07_stop_container(self):
        oc = OwtfContainer(self.container_location)
        self.assertTrue(oc.is_running)
        oc.stop()
        self.assertFalse(oc.is_running)
        self.assertFalse(oc.container_id in [i['Id'] for i in cli.containers()])

    def test_08_remove_image_and_container(self):
        oc = OwtfContainer(self.container_location)
        self.assertTrue(oc.is_container_build)
        self.assertTrue(oc.is_image_build)
        oc.remove_container()
        self.assertFalse(oc.is_container_build)
        self.assertFalse(oc.container_id in [i['Id'] for i in cli.containers(all=True)])
        oc.remove_image()
        self.assertFalse(oc.is_image_build)
        self.assertFalse(oc.image_id in [i['Id'] for i in cli.images()])


if __name__ == '__main__':
    unittest.main()

