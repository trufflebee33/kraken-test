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

from kraken_sdk.models.update_domain_request import UpdateDomainRequest

class TestUpdateDomainRequest(unittest.TestCase):
    """UpdateDomainRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateDomainRequest:
        """Test UpdateDomainRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateDomainRequest`
        """
        model = UpdateDomainRequest()
        if include_optional:
            return UpdateDomainRequest(
                comment = '',
                global_tags = [
                    ''
                    ],
                workspace_tags = [
                    ''
                    ]
            )
        else:
            return UpdateDomainRequest(
        )
        """

    def testUpdateDomainRequest(self):
        """Test UpdateDomainRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
