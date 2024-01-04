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
from graalsystems.model.cran_library import CranLibrary
from graalsystems.model.file_library import FileLibrary
from graalsystems.model.git_library import GitLibrary
from graalsystems.model.library import Library
from graalsystems.model.maven_library import MavenLibrary
from graalsystems.model.maven_library_all_of import MavenLibraryAllOf
from graalsystems.model.py_pi_library import PyPiLibrary
globals()['CranLibrary'] = CranLibrary
globals()['FileLibrary'] = FileLibrary
globals()['GitLibrary'] = GitLibrary
globals()['Library'] = Library
globals()['MavenLibrary'] = MavenLibrary
globals()['MavenLibraryAllOf'] = MavenLibraryAllOf
globals()['PyPiLibrary'] = PyPiLibrary
from graalsystems.model.maven_library import MavenLibrary


class TestMavenLibrary(unittest.TestCase):
    """MavenLibrary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMavenLibrary(self):
        """Test MavenLibrary"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MavenLibrary()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
