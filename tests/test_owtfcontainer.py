
import unittest
from owtfvalhalla.owtfcontainer import OwtfContainer
from owtfvalhalla.dclient import dclient


class OwtfContainerTest(unittest.TestCase):

    def setUp(self):
        oc = OwtfContainer('/Users/nils/Desktop/owtf-valhalla/owtfvalhalla/containers/testcontainer')
        if oc.container_tag in [i['RepoTags'][0] for i in dclient.images()]:
            oc.remove_image()

        if '/'+oc.container_name+'_'+oc.container_version in [i['Names'][0] for i in dclient.containers(all=True)]:
            oc.remove_container()

    def tearDown(self):
        oc = OwtfContainer('/Users/nils/Desktop/owtf-valhalla/owtfvalhalla/containers/testcontainer')
        if oc.container_tag in [i['RepoTags'][0] for i in dclient.images()]:
            oc.remove_image()

        if '/' + oc.container_name + '_' + oc.container_version in [i['Names'][0] for i in dclient.containers(all=True)]:
            oc.remove_container()

    def test_validate_true(self):
        oc = OwtfContainer('/Users/nils/Desktop/owtf-valhalla/owtfvalhalla/containers/testcontainer')
        self.assertTrue(oc.is_valid)

    def test_readconfigfile_true(self):
        oc = OwtfContainer('/Users/nils/Desktop/owtf-valhalla/owtfvalhalla/containers/testcontainer')
        self.assertTrue(oc.read_config_file())

    def test_buildingimage_true(self):
        oc = OwtfContainer('/Users/nils/Desktop/owtf-valhalla/owtfvalhalla/containers/testcontainer')
        oc.build_image()
        self.assertTrue(oc.is_image_build)
        self.assertTrue(oc.container_tag in [i['RepoTags'][0] for i in dclient.images()])

    def test_removeimage_true(self):
        oc = OwtfContainer('/Users/nils/Desktop/owtf-valhalla/owtfvalhalla/containers/testcontainer')
        oc.build_image()
        self.assertTrue(oc.is_image_build)
        oc.remove_image()
        self.assertFalse(oc.is_image_build)
        self.assertFalse(oc.container_tag in [i['RepoTags'][0] for i in dclient.images()])

    def test_buildcontainer_true(self):
        oc = OwtfContainer('/Users/nils/Desktop/owtf-valhalla/owtfvalhalla/containers/testcontainer')
        if oc.is_running or oc.is_container_build:
            oc.stop()
            self.assertFalse(oc.is_running)
            oc.remove_container()
            self.assertFalse(oc.is_container_build)
        oc.build_image()
        self.assertTrue(oc.is_image_build)
        oc.build_container()
        self.assertTrue(oc.is_container_build)
        self.assertTrue(oc.container_tag in [i['Image'] for i in dclient.containers(all=True)])

    def test_removecontainer_true(self):
        oc = OwtfContainer('/Users/nils/Desktop/owtf-valhalla/owtfvalhalla/containers/testcontainer')
        if not oc.is_container_build:
            oc.build_image()
            oc.build_container()
            self.assertTrue(oc.is_image_build)
            self.assertTrue(oc.is_container_build)
        oc.remove_container()
        self.assertFalse(oc.is_container_build)
        self.assertFalse(oc.container_tag in [i['Image'] for i in dclient.containers(all=True)])












