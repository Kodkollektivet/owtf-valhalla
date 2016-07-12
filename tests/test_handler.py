import unittest
from valhalla.dockerutils import handler
from valhalla.dockerutils.owtfcontainer import OwtfContainer
from valhalla.django.settings.settings import CONTAINER_DIR


class OwtfContainerTest(unittest.TestCase):

    def test_verifytypes_true(self):
        ocs = handler.get_valhalla_container()
        self.assertTrue(isinstance(ocs[0], bool))
        self.assertTrue(isinstance(ocs[1], list))

    def test_test_true(self):  # Test that the test can find containers
        self.assertTrue(len(handler._containers) > 0)

    def test_image_true(self):
        self.assertTrue(handler.get_valhalla_container(image='owtfvalhallatestcontainer:0.1')[0])
        self.assertTrue(isinstance(handler.get_valhalla_container(image='owtfvalhallatestcontainer:0.1')[1], OwtfContainer))

    def test_image_false(self):
        status, container = handler.get_valhalla_container(image='doesnotexists:0.1')
        self.assertFalse(status)

    def test_to_many_arguments_false(self):
        # To many arguments, function accepts only one.
        self.assertFalse(handler.get_valhalla_container(image='a', image_id=0, container_id=0)[0])

    def test_container_id_true(self):
        """Get a image by image and then check it can be found via container_id"""
        status, container = handler.get_valhalla_container(image='owtfvalhallatestcontainer:0.1')
        self.assertTrue(status)
        c_id = container.container_id
        status, container = handler.get_valhalla_container(container_id=c_id)
        self.assertTrue(status)

    def test_container_id_false(self):
        self.assertFalse(handler.get_valhalla_container(container_id=0)[0])

    def test_image_id_true(self):
        c = handler.get_valhalla_container(image='owtfvalhallatestcontainer:0.1')[1]
        self.assertTrue(handler.get_valhalla_container(image_id=c.image_id)[0])

