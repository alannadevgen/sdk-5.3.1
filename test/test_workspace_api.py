"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import graalsystems
from graalsystems.api.workspace_api import WorkspaceApi  # noqa: E501


class TestWorkspaceApi(unittest.TestCase):
    """WorkspaceApi unit test stubs"""

    def setUp(self):
        self.api = WorkspaceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_workspace(self):
        """Test case for create_workspace

        Create workspace  # noqa: E501
        """
        pass

    def test_delete_workspace_by_id(self):
        """Test case for delete_workspace_by_id

        Delete a workspace by an id  # noqa: E501
        """
        pass

    def test_find_workspace_by_id(self):
        """Test case for find_workspace_by_id

        Find workspace by Id  # noqa: E501
        """
        pass

    def test_find_workspaces(self):
        """Test case for find_workspaces

        Retrieve all workspaces  # noqa: E501
        """
        pass

    def test_get_logs_for_workspace(self):
        """Test case for get_logs_for_workspace

        Get logs  # noqa: E501
        """
        pass

    def test_update_workspace(self):
        """Test case for update_workspace

        Update a workspace  # noqa: E501
        """
        pass

    def test_upload_file_in_workspace(self):
        """Test case for upload_file_in_workspace

        Upload files in a workspace  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
