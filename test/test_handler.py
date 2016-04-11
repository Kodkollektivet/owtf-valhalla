import unittest
from core.dockerutils import *


class OwtfContainerTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_verifytypes_true(self):
        ocs = get_owtf_c()
        self.assertTrue(isinstance(ocs[0], bool))
        self.assertTrue(isinstance(ocs[1], list))


