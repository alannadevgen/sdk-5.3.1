"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import graalsystems
from graalsystems.api.env_api import EnvApi  # noqa: E501


class TestEnvApi(unittest.TestCase):
    """EnvApi unit test stubs"""

    def setUp(self):
        self.api = EnvApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_capacity(self):
        """Test case for get_capacity

        Retrieve the capacity  # noqa: E501
        """
        pass

    def test_get_endpoints(self):
        """Test case for get_endpoints

        Find the endpoints for the current tenant  # noqa: E501
        """
        pass

    def test_get_env(self):
        """Test case for get_env

        Retrieve the current tenant  # noqa: E501
        """
        pass

    def test_get_metrics_for_tenant(self):
        """Test case for get_metrics_for_tenant

        Find the metrics for the current tenant  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()