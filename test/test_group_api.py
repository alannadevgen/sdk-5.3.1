"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import graalsystems
from graalsystems.api.group_api import GroupApi  # noqa: E501


class TestGroupApi(unittest.TestCase):
    """GroupApi unit test stubs"""

    def setUp(self):
        self.api = GroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_group(self):
        """Test case for create_group

        Create a group  # noqa: E501
        """
        pass

    def test_delete_group_by_id(self):
        """Test case for delete_group_by_id

        Delete an group by an id  # noqa: E501
        """
        pass

    def test_find_group_by_id(self):
        """Test case for find_group_by_id

        Find group by Id  # noqa: E501
        """
        pass

    def test_find_groups(self):
        """Test case for find_groups

        Retrieve all groups  # noqa: E501
        """
        pass

    def test_find_roles_by_group_id(self):
        """Test case for find_roles_by_group_id

        Find roles by a group id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()