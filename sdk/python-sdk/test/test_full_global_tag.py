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

from kraken_sdk.models.full_global_tag import FullGlobalTag

class TestFullGlobalTag(unittest.TestCase):
    """FullGlobalTag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FullGlobalTag:
        """Test FullGlobalTag
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FullGlobalTag`
        """
        model = FullGlobalTag()
        if include_optional:
            return FullGlobalTag(
                uuid = '',
                name = '',
                color = kraken_sdk.models.color.Color(
                    r = 0, 
                    g = 0, 
                    b = 0, 
                    a = 0, )
            )
        else:
            return FullGlobalTag(
                uuid = '',
                name = '',
                color = kraken_sdk.models.color.Color(
                    r = 0, 
                    g = 0, 
                    b = 0, 
                    a = 0, ),
        )
        """

    def testFullGlobalTag(self):
        """Test FullGlobalTag"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
