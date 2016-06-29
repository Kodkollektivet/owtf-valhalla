import unittest
from core.dockerutils import handler
from core.dockerutils.owtfcontainer import OwtfContainer


class OwtfContainerTest(unittest.TestCase):

    def setUp(self):
        handler.locate_owtf_containers('../containers')

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
        c_id = handler.get_owtf_c(image='owtfvalhallatestcontainer:0.1')[1].container_id
        self.assertTrue(handler.get_owtf_c(container_id=c_id)[0])

    def test_container_id_false(self):
        self.assertFalse(handler.get_owtf_c(container_id=0)[0])

    # TODO: image_id when image is buid does not assign correctly.
    # def test_image_id_true(self):
    #     c = handler.get_owtf_c(image='owtfvalhallatestcontainer:0.1')[1]
    #     c.build_image()
    #     image_id = c.image_id
    #     self.assertTrue(handler.get_owtf_c(image_id=image_id)[0])

