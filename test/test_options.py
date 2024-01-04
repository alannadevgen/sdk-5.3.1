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
from graalsystems.model.airflow_options import AirflowOptions
from graalsystems.model.bash_options import BashOptions
from graalsystems.model.dask_options import DaskOptions
from graalsystems.model.database_migration_options import DatabaseMigrationOptions
from graalsystems.model.dbt_options import DbtOptions
from graalsystems.model.flink_options import FlinkOptions
from graalsystems.model.hadoop_options import HadoopOptions
from graalsystems.model.knime_options import KnimeOptions
from graalsystems.model.low_code_options import LowCodeOptions
from graalsystems.model.mx_net_options import MXNetOptions
from graalsystems.model.py_torch_options import PyTorchOptions
from graalsystems.model.python_options import PythonOptions
from graalsystems.model.ray_options import RayOptions
from graalsystems.model.sas_options import SASOptions
from graalsystems.model.spark_options import SparkOptions
from graalsystems.model.tensorflow_options import TensorflowOptions
from graalsystems.model.xgboost_options import XgboostOptions
globals()['AirflowOptions'] = AirflowOptions
globals()['BashOptions'] = BashOptions
globals()['DaskOptions'] = DaskOptions
globals()['DatabaseMigrationOptions'] = DatabaseMigrationOptions
globals()['DbtOptions'] = DbtOptions
globals()['FlinkOptions'] = FlinkOptions
globals()['HadoopOptions'] = HadoopOptions
globals()['KnimeOptions'] = KnimeOptions
globals()['LowCodeOptions'] = LowCodeOptions
globals()['MXNetOptions'] = MXNetOptions
globals()['PyTorchOptions'] = PyTorchOptions
globals()['PythonOptions'] = PythonOptions
globals()['RayOptions'] = RayOptions
globals()['SASOptions'] = SASOptions
globals()['SparkOptions'] = SparkOptions
globals()['TensorflowOptions'] = TensorflowOptions
globals()['XgboostOptions'] = XgboostOptions
from graalsystems.model.options import Options


class TestOptions(unittest.TestCase):
    """Options unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOptions(self):
        """Test Options"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Options()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
