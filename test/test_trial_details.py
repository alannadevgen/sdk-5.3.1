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
from graalsystems.model.credit_card_details import CreditCardDetails
from graalsystems.model.details1 import Details1
from graalsystems.model.in_person_details import InPersonDetails
from graalsystems.model.sepa_details import SepaDetails
from graalsystems.model.trial_details import TrialDetails
from graalsystems.model.trial_details_all_of import TrialDetailsAllOf
globals()['CreditCardDetails'] = CreditCardDetails
globals()['Details1'] = Details1
globals()['InPersonDetails'] = InPersonDetails
globals()['SepaDetails'] = SepaDetails
globals()['TrialDetails'] = TrialDetails
globals()['TrialDetailsAllOf'] = TrialDetailsAllOf
from graalsystems.model.trial_details import TrialDetails


class TestTrialDetails(unittest.TestCase):
    """TrialDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTrialDetails(self):
        """Test TrialDetails"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TrialDetails()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
