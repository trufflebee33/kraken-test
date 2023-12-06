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

from kraken_sdk.api.user_admin_management_api import UserAdminManagementApi


class TestUserAdminManagementApi(unittest.TestCase):
    """UserAdminManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserAdminManagementApi()

    def tearDown(self) -> None:
        pass

    def test_create_user(self) -> None:
        """Test case for create_user

        Create a user
        """
        pass

    def test_delete_user(self) -> None:
        """Test case for delete_user

        Delete a user by its uuid
        """
        pass

    def test_get_all_users_admin(self) -> None:
        """Test case for get_all_users_admin

        Retrieve all users
        """
        pass

    def test_get_user(self) -> None:
        """Test case for get_user

        Retrieve a user by its uuid
        """
        pass


if __name__ == '__main__':
    unittest.main()
