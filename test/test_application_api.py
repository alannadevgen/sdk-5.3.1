"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import graalsystems
from graalsystems.api.application_api import ApplicationApi  # noqa: E501


class TestApplicationApi(unittest.TestCase):
    """ApplicationApi unit test stubs"""

    def setUp(self):
        self.api = ApplicationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_application(self):
        """Test case for create_application

        Create a application  # noqa: E501
        """
        pass

    def test_delete_application_by_id(self):
        """Test case for delete_application_by_id

        Delete an application by an id  # noqa: E501
        """
        pass

    def test_find_application_by_id(self):
        """Test case for find_application_by_id

        Find application by Id  # noqa: E501
        """
        pass

    def test_find_applications(self):
        """Test case for find_applications

        Retrieve all applications  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()