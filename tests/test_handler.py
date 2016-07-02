import unittest
from valhalla.dockerutils import handler
from valhalla.dockerutils.owtfcontainer import OwtfContainer
from valhalla.django.settings.settings import CONTAINER_DIR


class OwtfContainerTest(unittest.TestCase):

    def setUp(self):
        pass
        #handler.locate_owtf_containers('../containers')

    def tearDown(self):
        pass

    def test_verifytypes_true(self):
        ocs = handler.get_owtf_c()
        self.assertTrue(isinstance(ocs[0], bool))
        self.assertTrue(isinstance(ocs[1], list))

    def test_test_true(self):  # Test that the test can find containers
        self.assertTrue(len(handler._containers) > 0)

    def test_image_true(self):
        self.assertTrue(handler.get_owtf_c(image='owtfvalhallatestcontainer:0.1')[0])
        self.assertTrue(isinstance(handler.get_owtf_c(image='owtfvalhallatestcontainer:0.1')[1], OwtfContainer))

    def test_image_false(self):
        self.assertFalse(handler.get_owtf_c(image='doesnotexists:0.1')[0])

    def test_to_many_arguments_false(self):
        # To many arguments, function accepts only one.
        self.assertFalse(handler.get_owtf_c(image='a', image_id=0, container_id=0)[0])

    def test_container_id_true(self):
        c = handler.get_owtf_c(image='owtfvalhallatestcontainer:0.1')[1]
        c_id = c.container_id
        self.assertTrue(handler.get_owtf_c(container_id=c_id))

    def test_container_id_false(self):
        self.assertFalse(handler.get_owtf_c(container_id=0)[0])

    def test_image_id_true(self):
        c = handler.get_owtf_c(image='owtfvalhallatestcontainer:0.1')[1]
        self.assertTrue(handler.get_owtf_c(image_id=c.image_id)[0])

