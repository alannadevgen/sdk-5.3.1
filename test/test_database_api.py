"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import graalsystems
from graalsystems.api.database_api import DatabaseApi  # noqa: E501


class TestDatabaseApi(unittest.TestCase):
    """DatabaseApi unit test stubs"""

    def setUp(self):
        self.api = DatabaseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_database(self):
        """Test case for create_database

        Create a database  # noqa: E501
        """
        pass

    def test_delete_database_by_id(self):
        """Test case for delete_database_by_id

        Delete a database by an id  # noqa: E501
        """
        pass

    def test_find_database_by_id(self):
        """Test case for find_database_by_id

        Find database by Id  # noqa: E501
        """
        pass

    def test_find_databases(self):
        """Test case for find_databases

        Retrieve all databases  # noqa: E501
        """
        pass

    def test_update_database(self):
        """Test case for update_database

        Update a database  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
