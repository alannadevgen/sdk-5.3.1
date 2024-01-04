"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import graalsystems
from graalsystems.api.identity_api import IdentityApi  # noqa: E501


class TestIdentityApi(unittest.TestCase):
    """IdentityApi unit test stubs"""

    def setUp(self):
        self.api = IdentityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_identity(self):
        """Test case for create_identity

        Create a identity  # noqa: E501
        """
        pass

    def test_delete_identity_by_id(self):
        """Test case for delete_identity_by_id

        Delete an identity by an id  # noqa: E501
        """
        pass

    def test_find_identities(self):
        """Test case for find_identities

        Retrieve all identities  # noqa: E501
        """
        pass

    def test_find_identity_by_id(self):
        """Test case for find_identity_by_id

        Find identity by Id  # noqa: E501
        """
        pass

    def test_find_roles_by_identity_id(self):
        """Test case for find_roles_by_identity_id

        Find roles by a identity id  # noqa: E501
        """
        pass

    def test_update_identity(self):
        """Test case for update_identity

        Update a identity  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()