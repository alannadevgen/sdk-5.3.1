"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import graalsystems
from graalsystems.api.stripe_api import StripeApi  # noqa: E501


class TestStripeApi(unittest.TestCase):
    """StripeApi unit test stubs"""

    def setUp(self):
        self.api = StripeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_stripe_create_setup_intent(self):
        """Test case for stripe_create_setup_intent

        create setup intent on Stripe  # noqa: E501
        """
        pass

    def test_stripe_public_key(self):
        """Test case for stripe_public_key

        get Stripe public key  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()