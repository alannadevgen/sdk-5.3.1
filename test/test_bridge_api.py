"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import graalsystems
from graalsystems.api.bridge_api import BridgeApi  # noqa: E501


class TestBridgeApi(unittest.TestCase):
    """BridgeApi unit test stubs"""

    def setUp(self):
        self.api = BridgeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_bridge(self):
        """Test case for create_bridge

        Create bridge  # noqa: E501
        """
        pass

    def test_delete_bridge_by_id(self):
        """Test case for delete_bridge_by_id

        Delete a bridge by an id  # noqa: E501
        """
        pass

    def test_find_bridge_by_id(self):
        """Test case for find_bridge_by_id

        Find bridge by Id  # noqa: E501
        """
        pass

    def test_find_bridges(self):
        """Test case for find_bridges

        Retrieve all bridges  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
