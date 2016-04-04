
import unittest
from owtfvalhalla.owtfcontainer import OwtfContainer
from owtfvalhalla.owtfcontainer.dclient import *


class OwtfContainerTest(unittest.TestCase):

    def setUp(self):
        oc = OwtfContainer('../owtfvalhalla/containers/testcontainer')
        if oc.image_id in [i['Id'] for i in cli.images()]:
            oc.remove_image()

        if oc.container_id in [i['Id'] for i in cli.containers(all=True)]:
            oc.remove_container()

    def tearDown(self):
        oc = OwtfContainer('../owtfvalhalla/containers/testcontainer')
        if oc.image_id in [i['Id'] for i in cli.images()]:
            oc.remove_image()

        if oc.container_id in [i['Id'] for i in cli.containers(all=True)]:
            oc.remove_container()

    def test_validate_true(self):
        oc = OwtfContainer('../owtfvalhalla/containers/testcontainer')
        self.assertTrue(oc.is_valid)

    def test_buildingimage_true(self):
        oc = OwtfContainer('../owtfvalhalla/containers/testcontainer')
        self.assertTrue(oc.is_valid)
        oc.build_image()
        self.assertTrue(oc.is_image_build)
        self.assertTrue(oc.image_id in [i['Id'] for i in cli.images()])

    def test_removeimage_true(self):
        oc = OwtfContainer('../owtfvalhalla/containers/testcontainer')
        oc.build_image()
        self.assertTrue(oc.is_image_build)
        oc.remove_image()
        self.assertFalse(oc.is_image_build)
        self.assertFalse(oc.image_id in [i['Id'] for i in cli.images()])

    def test_buildcontainer_true(self):
        oc = OwtfContainer('../owtfvalhalla/containers/testcontainer')
        if oc.is_running and oc.is_container_build:
            oc.stop()
            self.assertFalse(oc.is_running)
            oc.remove_container()
            self.assertFalse(oc.is_container_build)
        oc.build_image()
        self.assertTrue(oc.is_image_build)
        oc.build_container()
        self.assertTrue(oc.is_container_build)
        self.assertTrue(oc.container_id in [i['Id'] for i in cli.containers(all=True)])

    def test_removecontainer_true(self):
        oc = OwtfContainer('../owtfvalhalla/containers/testcontainer')
        if not oc.is_container_build:
            oc.build_image()
            oc.build_container()
            self.assertTrue(oc.is_image_build)
            self.assertTrue(oc.is_container_build)
        oc.remove_container()
        self.assertFalse(oc.is_container_build)
        self.assertFalse(oc.container_id in [i['Id'] for i in cli.containers(all=True)])

    def test_startcommandsstop_true(self):
        oc = OwtfContainer('../owtfvalhalla/containers/testcontainer')
        oc.build_image()
        self.assertTrue(oc.is_image_build)
        oc.build_container()
        self.assertTrue(oc.is_container_build)
        oc.start()
        self.assertTrue(oc.is_running)
        self.assertTrue(oc.container_id in [i['Id'] for i in cli.containers()])
        commands = '[{"command": "sleep 5s", "code": "666", "type": "passive"}, {"command": "ls -la", "code": "667", "type": "active"}, {"command": "sleep 5s", "code": "668", "type": "semi-passive"}, {"command": "sleep 5s", "code": "669", "type": "semi-active"}]'
        self.assertEqual(oc.get_available_commands(), commands)
        oc.stop()
        self.assertFalse(oc.container_id in [i['Id'] for i in cli.containers()])
        self.assertFalse(oc.is_running)

if __name__ == '__main__':
    unittest.main()












