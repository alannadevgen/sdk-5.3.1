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
from graalsystems.model.end_task import EndTask
from graalsystems.model.error_task import ErrorTask
from graalsystems.model.job_task import JobTask
from graalsystems.model.script_task import ScriptTask
from graalsystems.model.script_task_all_of import ScriptTaskAllOf
from graalsystems.model.start_task import StartTask
from graalsystems.model.task import Task
from graalsystems.model.workflow_task import WorkflowTask
globals()['EndTask'] = EndTask
globals()['ErrorTask'] = ErrorTask
globals()['JobTask'] = JobTask
globals()['ScriptTask'] = ScriptTask
globals()['ScriptTaskAllOf'] = ScriptTaskAllOf
globals()['StartTask'] = StartTask
globals()['Task'] = Task
globals()['WorkflowTask'] = WorkflowTask
from graalsystems.model.script_task import ScriptTask


class TestScriptTask(unittest.TestCase):
    """ScriptTask unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testScriptTask(self):
        """Test ScriptTask"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ScriptTask()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
