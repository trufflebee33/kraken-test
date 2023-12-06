# coding: utf-8

"""
    kraken

    The core component of kraken-project

    The version of the OpenAPI document: 0.1.0
    Contact: git@omikron.dev
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from kraken_sdk.models.simple_host import SimpleHost

class TestSimpleHost(unittest.TestCase):
    """SimpleHost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimpleHost:
        """Test SimpleHost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimpleHost`
        """
        model = SimpleHost()
        if include_optional:
            return SimpleHost(
                uuid = '',
                ip_addr = '172.0.0.1',
                os_type = 'Unknown',
                comment = '',
                workspace = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return SimpleHost(
                uuid = '',
                ip_addr = '172.0.0.1',
                os_type = 'Unknown',
                comment = '',
                workspace = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testSimpleHost(self):
        """Test SimpleHost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
