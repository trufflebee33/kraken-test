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

from kraken_sdk.models.update_wordlist_request import UpdateWordlistRequest

class TestUpdateWordlistRequest(unittest.TestCase):
    """UpdateWordlistRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateWordlistRequest:
        """Test UpdateWordlistRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateWordlistRequest`
        """
        model = UpdateWordlistRequest()
        if include_optional:
            return UpdateWordlistRequest(
                uuid = '',
                name = 'subdomains-top1million-5000.txt',
                description = 'List of 5000 subdomains',
                path = '/opt/wordlists/Discovery/DNS/subdomains-top1million-5000.txt'
            )
        else:
            return UpdateWordlistRequest(
                uuid = '',
        )
        """

    def testUpdateWordlistRequest(self):
        """Test UpdateWordlistRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
