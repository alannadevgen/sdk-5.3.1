"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import graalsystems
from graalsystems.api.notification_api import NotificationApi  # noqa: E501


class TestNotificationApi(unittest.TestCase):
    """NotificationApi unit test stubs"""

    def setUp(self):
        self.api = NotificationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_notification(self):
        """Test case for create_notification

        Create a notification  # noqa: E501
        """
        pass

    def test_find_notifications(self):
        """Test case for find_notifications

        Retrieve all notifications  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()