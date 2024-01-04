"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import graalsystems
from graalsystems.api.job_api import JobApi  # noqa: E501


class TestJobApi(unittest.TestCase):
    """JobApi unit test stubs"""

    def setUp(self):
        self.api = JobApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_job_by_id(self):
        """Test case for delete_job_by_id

        Delete a job by its id  # noqa: E501
        """
        pass

    def test_find_job_by_job_id(self):
        """Test case for find_job_by_job_id

        Find job by Id  # noqa: E501
        """
        pass

    def test_find_jobs(self):
        """Test case for find_jobs

        Retrieve all jobs  # noqa: E501
        """
        pass

    def test_get_metrics_for_job(self):
        """Test case for get_metrics_for_job

        Find the metrics for a job  # noqa: E501
        """
        pass

    def test_get_stats_by_job_id(self):
        """Test case for get_stats_by_job_id

        Find the stats for a job  # noqa: E501
        """
        pass

    def test_update_job(self):
        """Test case for update_job

        Update a job  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
