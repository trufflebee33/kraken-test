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

from kraken_sdk.models.full_workspace_invitation import FullWorkspaceInvitation

class TestFullWorkspaceInvitation(unittest.TestCase):
    """FullWorkspaceInvitation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FullWorkspaceInvitation:
        """Test FullWorkspaceInvitation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FullWorkspaceInvitation`
        """
        model = FullWorkspaceInvitation()
        if include_optional:
            return FullWorkspaceInvitation(
                uuid = '',
                workspace = kraken_sdk.models.simple_workspace.SimpleWorkspace(
                    uuid = '', 
                    name = 'ultra-secure-workspace', 
                    description = 'This workspace is ultra secure and should not be looked at!!', 
                    owner = kraken_sdk.models.simple_user.SimpleUser(
                        uuid = '', 
                        username = '', 
                        display_name = '', ), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                var_from = kraken_sdk.models.simple_user.SimpleUser(
                    uuid = '', 
                    username = '', 
                    display_name = '', ),
                target = kraken_sdk.models.simple_user.SimpleUser(
                    uuid = '', 
                    username = '', 
                    display_name = '', )
            )
        else:
            return FullWorkspaceInvitation(
                uuid = '',
                workspace = kraken_sdk.models.simple_workspace.SimpleWorkspace(
                    uuid = '', 
                    name = 'ultra-secure-workspace', 
                    description = 'This workspace is ultra secure and should not be looked at!!', 
                    owner = kraken_sdk.models.simple_user.SimpleUser(
                        uuid = '', 
                        username = '', 
                        display_name = '', ), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                var_from = kraken_sdk.models.simple_user.SimpleUser(
                    uuid = '', 
                    username = '', 
                    display_name = '', ),
                target = kraken_sdk.models.simple_user.SimpleUser(
                    uuid = '', 
                    username = '', 
                    display_name = '', ),
        )
        """

    def testFullWorkspaceInvitation(self):
        """Test FullWorkspaceInvitation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
