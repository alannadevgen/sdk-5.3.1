"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graalsystems
from graalsystems.model.azure_uri import AzureUri
from graalsystems.model.azure_uri_all_of import AzureUriAllOf
from graalsystems.model.generic_uri import GenericUri
from graalsystems.model.s3_uri import S3Uri
from graalsystems.model.uri import Uri
globals()['AzureUri'] = AzureUri
globals()['AzureUriAllOf'] = AzureUriAllOf
globals()['GenericUri'] = GenericUri
globals()['S3Uri'] = S3Uri
globals()['Uri'] = Uri
from graalsystems.model.azure_uri import AzureUri


class TestAzureUri(unittest.TestCase):
    """AzureUri unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAzureUri(self):
        """Test AzureUri"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AzureUri()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
