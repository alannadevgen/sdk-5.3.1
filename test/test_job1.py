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
from graalsystems.model.job1_all_of import Job1AllOf
from graalsystems.model.project1 import Project1
from graalsystems.model.resource import Resource
globals()['Job1AllOf'] = Job1AllOf
globals()['Project1'] = Project1
globals()['Resource'] = Resource
from graalsystems.model.job1 import Job1


class TestJob1(unittest.TestCase):
    """Job1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJob1(self):
        """Test Job1"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Job1()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()