import unittest
from nose.tools import timed
from valhalla.dockerutils.owtfcontainer import OwtfContainer
from valhalla.middleman import send_for_execution


class MiddlemanHandlerTest(unittest.TestCase):

    @unittest.skip('Work in progress')
    def test_send_simple_command_for_execition(self):
        oc = OwtfContainer('valhalla/containers/testcontainer')
        oc.build_image()
        oc.build_container()
        oc.start()
        self.assertTrue(oc.is_running)
        res = send_for_execution(oc, {'command': 'ping -c 1 scanme.nmap.org'})
        self.assertTrue(isinstance(res, dict))
