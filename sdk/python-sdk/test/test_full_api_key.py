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

from kraken_sdk.models.full_api_key import FullApiKey

class TestFullApiKey(unittest.TestCase):
    """FullApiKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FullApiKey:
        """Test FullApiKey
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FullApiKey`
        """
        model = FullApiKey()
        if include_optional:
            return FullApiKey(
                uuid = '',
                name = 'Leech on my local machine',
                key = 'fsn83r0jfis84nfthw...'
            )
        else:
            return FullApiKey(
                uuid = '',
                name = 'Leech on my local machine',
                key = 'fsn83r0jfis84nfthw...',
        )
        """

    def testFullApiKey(self):
        """Test FullApiKey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
