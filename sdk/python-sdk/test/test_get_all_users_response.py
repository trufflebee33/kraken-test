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

from kraken_sdk.models.get_all_users_response import GetAllUsersResponse

class TestGetAllUsersResponse(unittest.TestCase):
    """GetAllUsersResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAllUsersResponse:
        """Test GetAllUsersResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAllUsersResponse`
        """
        model = GetAllUsersResponse()
        if include_optional:
            return GetAllUsersResponse(
                users = [
                    kraken_sdk.models.simple_user.SimpleUser(
                        uuid = '', 
                        username = '', 
                        display_name = '', )
                    ]
            )
        else:
            return GetAllUsersResponse(
                users = [
                    kraken_sdk.models.simple_user.SimpleUser(
                        uuid = '', 
                        username = '', 
                        display_name = '', )
                    ],
        )
        """

    def testGetAllUsersResponse(self):
        """Test GetAllUsersResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
