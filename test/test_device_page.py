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
from graalsystems.model.device import Device
from graalsystems.model.device_page_all_of import DevicePageAllOf
from graalsystems.model.page import Page
globals()['Device'] = Device
globals()['DevicePageAllOf'] = DevicePageAllOf
globals()['Page'] = Page
from graalsystems.model.device_page import DevicePage


class TestDevicePage(unittest.TestCase):
    """DevicePage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDevicePage(self):
        """Test DevicePage"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DevicePage()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
