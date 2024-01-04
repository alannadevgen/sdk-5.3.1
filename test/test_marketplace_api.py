"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import graalsystems
from graalsystems.api.marketplace_api import MarketplaceApi  # noqa: E501


class TestMarketplaceApi(unittest.TestCase):
    """MarketplaceApi unit test stubs"""

    def setUp(self):
        self.api = MarketplaceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_find_template_metadata(self):
        """Test case for find_template_metadata

        Get template metadata  # noqa: E501
        """
        pass

    def test_find_template_versions(self):
        """Test case for find_template_versions

        Get template versions  # noqa: E501
        """
        pass

    def test_find_templates(self):
        """Test case for find_templates

        Get templates  # noqa: E501
        """
        pass

    def test_generate_template(self):
        """Test case for generate_template

        Generate dag from a template  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()