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
from graalsystems.model.company import Company
from graalsystems.model.contact import Contact
globals()['Company'] = Company
globals()['Contact'] = Contact
from graalsystems.model.subscription import Subscription


class TestSubscription(unittest.TestCase):
    """Subscription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSubscription(self):
        """Test Subscription"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Subscription()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
