
import unittest
from owtfvalhalla.owtfcontainer import OwtfContainer


class OwtfContainerTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_validate_true(self):
        oc = OwtfContainer('/Users/nils/Desktop/owtf-valhalla/owtfvalhalla/containers/testcontainer')
        self.assertTrue(oc.is_valid)

    def test_readconfigfile_true(self):
        oc = OwtfContainer('/Users/nils/Desktop/owtf-valhalla/owtfvalhalla/containers/testcontainer')
        self.assertTrue(oc.read_config_file())







