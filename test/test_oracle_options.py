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
from graalsystems.model.data_warehouse_options import DataWarehouseOptions
from graalsystems.model.db2_options import DB2Options
from graalsystems.model.external_options import ExternalOptions
from graalsystems.model.maria_db_options import MariaDBOptions
from graalsystems.model.my_sql_options import MySQLOptions
from graalsystems.model.oracle_options import OracleOptions
from graalsystems.model.oracle_options_all_of import OracleOptionsAllOf
from graalsystems.model.postgre_sql_options import PostgreSQLOptions
from graalsystems.model.snowflake_options import SnowflakeOptions
from graalsystems.model.starburst_options import StarburstOptions
from graalsystems.model.synapse_options import SynapseOptions
from graalsystems.model.trino_options import TrinoOptions
globals()['DB2Options'] = DB2Options
globals()['DataWarehouseOptions'] = DataWarehouseOptions
globals()['ExternalOptions'] = ExternalOptions
globals()['MariaDBOptions'] = MariaDBOptions
globals()['MySQLOptions'] = MySQLOptions
globals()['OracleOptions'] = OracleOptions
globals()['OracleOptionsAllOf'] = OracleOptionsAllOf
globals()['PostgreSQLOptions'] = PostgreSQLOptions
globals()['SnowflakeOptions'] = SnowflakeOptions
globals()['StarburstOptions'] = StarburstOptions
globals()['SynapseOptions'] = SynapseOptions
globals()['TrinoOptions'] = TrinoOptions
from graalsystems.model.oracle_options import OracleOptions


class TestOracleOptions(unittest.TestCase):
    """OracleOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOracleOptions(self):
        """Test OracleOptions"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OracleOptions()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
