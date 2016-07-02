import unittest
import os
from valhalla.dockerutils import OwtfContainer
from valhalla.dockerutils.dclient import *
from valhalla.django.settings.settings import CONTAINER_DIR


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
        self.container_location = os.path.join(CONTAINER_DIR, 'testcontainer')

    def test_01_stop_remove_image_and_container(self):
        oc = OwtfContainer(self.container_location)

        oc.stop()
        self.assertFalse(oc.is_running)

        if oc.is_container_built:
            oc.remove_container()
            self.assertFalse(oc.is_container_built)

        if oc.is_image_built:
            oc.remove_image()
            self.assertFalse(oc.is_image_built)

        self.assertFalse(oc.is_image_built)
        self.assertFalse(oc.is_container_built)
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
        self.assertTrue(oc.is_image_built)
        self.assertTrue(oc.image_id in [i['Id'] for i in cli.images()])

    def test_05_build_container(self):
        oc = OwtfContainer(self.container_location)
        self.assertTrue(oc.is_image_built)
        self.assertFalse(oc.is_container_built)
        oc.build_container()
        self.assertTrue(oc.is_container_built)
        self.assertTrue(oc.container_id in [i['Id'] for i in cli.containers(all=True)])

    def test_06_start_contianer(self):
        oc = OwtfContainer(self.container_location)
        self.assertTrue(oc.is_image_built)
        self.assertTrue(oc.is_container_built)
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
        self.assertTrue(oc.is_container_built)
        self.assertTrue(oc.is_image_built)
        oc.remove_container()
        self.assertFalse(oc.is_container_built)
        self.assertFalse(oc.container_id in [i['Id'] for i in cli.containers(all=True)])
        oc.remove_image()
        self.assertFalse(oc.is_image_built)
        self.assertFalse(oc.image_id in [i['Id'] for i in cli.images()])


if __name__ == '__main__':
    unittest.main()

