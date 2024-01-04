"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import graalsystems
from graalsystems.api.library_api import LibraryApi  # noqa: E501


class TestLibraryApi(unittest.TestCase):
    """LibraryApi unit test stubs"""

    def setUp(self):
        self.api = LibraryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_library_by_id(self):
        """Test case for delete_library_by_id

        Delete a library by an id  # noqa: E501
        """
        pass

    def test_download_library(self):
        """Test case for download_library

        Download library by Id  # noqa: E501
        """
        pass

    def test_find_libraries(self):
        """Test case for find_libraries

        List all libraries  # noqa: E501
        """
        pass

    def test_find_metadata(self):
        """Test case for find_metadata

        Get library metadata by Id  # noqa: E501
        """
        pass

    def test_upload_library(self):
        """Test case for upload_library

        Upload a library  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
