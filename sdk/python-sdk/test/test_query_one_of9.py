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

from kraken_sdk.models.query_one_of9 import QueryOneOf9

class TestQueryOneOf9(unittest.TestCase):
    """QueryOneOf9 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryOneOf9:
        """Test QueryOneOf9
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueryOneOf9`
        """
        model = QueryOneOf9()
        if include_optional:
            return QueryOneOf9(
                address = None
            )
        else:
            return QueryOneOf9(
                address = None,
        )
        """

    def testQueryOneOf9(self):
        """Test QueryOneOf9"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
