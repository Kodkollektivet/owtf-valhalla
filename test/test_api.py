import json

from django.core.urlresolvers import resolve

from rest_framework.test import APITestCase


class TestApiViewsFunctionNames(APITestCase):
    """Test urls related to their function names."""

    def test_containers_func_name(self):
        route = resolve('/containers/')
        self.assertEqual(route.func.__name__, 'ListAll')


class TestApiContainerObject(APITestCase):
    """Test api conainer json objects."""

    def test_1_testcotainer_json_obj(self):
        response = self.client.get('/containers/owtfvalhallatestcontainer:0.1/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['image'], 'owtfvalhallatestcontainer:0.1')
        self.assertTrue(response.data['is_valid'])

    def test_2_testcotainer_json_build_image_true(self):
        response = self.client.get('/containers/owtfvalhallatestcontainer:0.1/build_image/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['image'], 'owtfvalhallatestcontainer:0.1')
        self.assertTrue(response.data['is_image_built'])

    def test_3_testcotainer_json_build_container_true(self):
        response = self.client.get('/containers/owtfvalhallatestcontainer:0.1/build_container/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['image'], 'owtfvalhallatestcontainer:0.1')
        self.assertTrue(response.data['is_container_built'])

    def test_4_testcotainer_json_start_container_true(self):
        response = self.client.get('/containers/owtfvalhallatestcontainer:0.1/start/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['image'], 'owtfvalhallatestcontainer:0.1')
        self.assertTrue(response.data['is_running'])

    def test_5_testcotainer_json_stop_container_true(self):
        response = self.client.get('/containers/owtfvalhallatestcontainer:0.1/stop/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['image'], 'owtfvalhallatestcontainer:0.1')
        self.assertFalse(response.data['is_running'])

    def test_6_testcotainer_json_remove_container_false(self):
        response = self.client.get('/containers/owtfvalhallatestcontainer:0.1/remove_container/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['image'], 'owtfvalhallatestcontainer:0.1')
        self.assertFalse(response.data['is_container_built'])

    def test_7_testcotainer_json_remove_container_false(self):
        response = self.client.get('/containers/owtfvalhallatestcontainer:0.1/remove_image/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['image'], 'owtfvalhallatestcontainer:0.1')
        self.assertFalse(response.data['is_image_built'])


class TestApiCommandsObject(APITestCase):
    """Test api conainer json objects."""

    def test_1_test_command_endpoint_status(self):
        response = self.client.get('/containers/commands/')
        self.assertEquals(response.status_code, 200)

    def test_2_test_command_endpoint_data(self):
        response = self.client.get('/containers/commands/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data[0]['code'], '666')
        self.assertEquals(response.data[0]['image'], 'owtfvalhallatestcontainer:0.1')
