"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import graalsystems
from graalsystems.api.data_api import DataApi  # noqa: E501


class TestDataApi(unittest.TestCase):
    """DataApi unit test stubs"""

    def setUp(self):
        self.api = DataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_files(self):
        """Test case for delete_files

        Delete files  # noqa: E501
        """
        pass

    def test_download_file(self):
        """Test case for download_file

        Download data by path  # noqa: E501
        """
        pass

    def test_get_data_files(self):
        """Test case for get_data_files

        Get files  # noqa: E501
        """
        pass

    def test_upload_file(self):
        """Test case for upload_file

        Upload a file  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
