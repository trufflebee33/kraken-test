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

from kraken_sdk.models.search_type_one_of4 import SearchTypeOneOf4

class TestSearchTypeOneOf4(unittest.TestCase):
    """SearchTypeOneOf4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchTypeOneOf4:
        """Test SearchTypeOneOf4
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchTypeOneOf4`
        """
        model = SearchTypeOneOf4()
        if include_optional:
            return SearchTypeOneOf4(
                var_and = [
                    null
                    ]
            )
        else:
            return SearchTypeOneOf4(
                var_and = [
                    null
                    ],
        )
        """

    def testSearchTypeOneOf4(self):
        """Test SearchTypeOneOf4"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
