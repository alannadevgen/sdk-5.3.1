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
from graalsystems.model.activity import Activity
from graalsystems.model.reaction import Reaction
from graalsystems.model.user1 import User1
from graalsystems.model.user_activity_all_of import UserActivityAllOf
globals()['Activity'] = Activity
globals()['Reaction'] = Reaction
globals()['User1'] = User1
globals()['UserActivityAllOf'] = UserActivityAllOf
from graalsystems.model.user_activity import UserActivity


class TestUserActivity(unittest.TestCase):
    """UserActivity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserActivity(self):
        """Test UserActivity"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserActivity()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()