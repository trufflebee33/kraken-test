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

from kraken_sdk.models.ws_message_one_of4 import WsMessageOneOf4

class TestWsMessageOneOf4(unittest.TestCase):
    """WsMessageOneOf4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WsMessageOneOf4:
        """Test WsMessageOneOf4
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WsMessageOneOf4`
        """
        model = WsMessageOneOf4()
        if include_optional:
            return WsMessageOneOf4(
                search_uuid = '',
                result_uuid = '',
                type = 'SearchNotify'
            )
        else:
            return WsMessageOneOf4(
                search_uuid = '',
                result_uuid = '',
                type = 'SearchNotify',
        )
        """

    def testWsMessageOneOf4(self):
        """Test WsMessageOneOf4"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
