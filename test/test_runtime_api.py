"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import graalsystems
from graalsystems.api.runtime_api import RuntimeApi  # noqa: E501


class TestRuntimeApi(unittest.TestCase):
    """RuntimeApi unit test stubs"""

    def setUp(self):
        self.api = RuntimeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_build_runtime_by_id(self):
        """Test case for build_runtime_by_id

        Find runtime by Id  # noqa: E501
        """
        pass

    def test_create_runtime(self):
        """Test case for create_runtime

        Create runtime  # noqa: E501
        """
        pass

    def test_delete_runtime_by_id(self):
        """Test case for delete_runtime_by_id

        Delete a runtime by an id  # noqa: E501
        """
        pass

    def test_find_build_by_runtime_id_and_build_id(self):
        """Test case for find_build_by_runtime_id_and_build_id

        Find the build by a runtimeId and a buildId  # noqa: E501
        """
        pass

    def test_find_builds_for_runtime(self):
        """Test case for find_builds_for_runtime

        Retrieve all builds for a runtime  # noqa: E501
        """
        pass

    def test_find_dependencies_by_runtime_id_and_version_id(self):
        """Test case for find_dependencies_by_runtime_id_and_version_id

        Find the dependencies by a runtimeId and a versionId  # noqa: E501
        """
        pass

    def test_find_runtime_by_id(self):
        """Test case for find_runtime_by_id

        Find runtime by Id  # noqa: E501
        """
        pass

    def test_find_runtimes(self):
        """Test case for find_runtimes

        Retrieve all runtimes  # noqa: E501
        """
        pass

    def test_find_version_by_runtime_id_and_version_id(self):
        """Test case for find_version_by_runtime_id_and_version_id

        Find the build by a runtimeId and a versionId  # noqa: E501
        """
        pass

    def test_find_versions_for_runtime(self):
        """Test case for find_versions_for_runtime

        Retrieve all versions for a runtime  # noqa: E501
        """
        pass

    def test_get_logs_for_build(self):
        """Test case for get_logs_for_build

        Get logs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()