"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import graalsystems
from graalsystems.api.role_api import RoleApi  # noqa: E501


class TestRoleApi(unittest.TestCase):
    """RoleApi unit test stubs"""

    def setUp(self):
        self.api = RoleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_role(self):
        """Test case for create_role

        Create a role  # noqa: E501
        """
        pass

    def test_delete_role_by_id(self):
        """Test case for delete_role_by_id

        Delete an role by an id  # noqa: E501
        """
        pass

    def test_find_current_roles(self):
        """Test case for find_current_roles

        Retrieve all roles for the current user  # noqa: E501
        """
        pass

    def test_find_permissions_by_role_id(self):
        """Test case for find_permissions_by_role_id

        Find permissions by role id  # noqa: E501
        """
        pass

    def test_find_role_by_id(self):
        """Test case for find_role_by_id

        Find role by Id  # noqa: E501
        """
        pass

    def test_find_roles(self):
        """Test case for find_roles

        Retrieve all roles  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
