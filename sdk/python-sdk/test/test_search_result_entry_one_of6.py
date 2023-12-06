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

from kraken_sdk.models.search_result_entry_one_of6 import SearchResultEntryOneOf6

class TestSearchResultEntryOneOf6(unittest.TestCase):
    """SearchResultEntryOneOf6 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchResultEntryOneOf6:
        """Test SearchResultEntryOneOf6
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchResultEntryOneOf6`
        """
        model = SearchResultEntryOneOf6()
        if include_optional:
            return SearchResultEntryOneOf6(
                dehashed_query_result_entry = kraken_sdk.models.simple_query_unhashed_result.SimpleQueryUnhashedResult(
                    uuid = '', 
                    attack = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    dehashed_id = 56, 
                    email = '', 
                    username = '', 
                    password = '', 
                    hashed_password = '', 
                    ip_address = '127.0.0.1', 
                    name = '', 
                    vin = '', 
                    address = '', 
                    phone = '', 
                    database_name = '', )
            )
        else:
            return SearchResultEntryOneOf6(
                dehashed_query_result_entry = kraken_sdk.models.simple_query_unhashed_result.SimpleQueryUnhashedResult(
                    uuid = '', 
                    attack = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    dehashed_id = 56, 
                    email = '', 
                    username = '', 
                    password = '', 
                    hashed_password = '', 
                    ip_address = '127.0.0.1', 
                    name = '', 
                    vin = '', 
                    address = '', 
                    phone = '', 
                    database_name = '', ),
        )
        """

    def testSearchResultEntryOneOf6(self):
        """Test SearchResultEntryOneOf6"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
