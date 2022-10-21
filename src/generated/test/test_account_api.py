"""
    @kin-kinetic/api

    The OpenAPI definition of the Kinetic API  # noqa: E501

    The version of the OpenAPI document: 1.0.0-rc.3
    Generated by: https://openapi-generator.tech
"""


import unittest

import kinetic_api_client
from kinetic_api_client.api.account_api import AccountApi  # noqa: E501


class TestAccountApi(unittest.TestCase):
    """AccountApi unit test stubs"""

    def setUp(self):
        self.api = AccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_account(self):
        """Test case for create_account

          # noqa: E501
        """
        pass

    def test_get_account_info(self):
        """Test case for get_account_info

          # noqa: E501
        """
        pass

    def test_get_balance(self):
        """Test case for get_balance

          # noqa: E501
        """
        pass

    def test_get_history(self):
        """Test case for get_history

          # noqa: E501
        """
        pass

    def test_get_token_accounts(self):
        """Test case for get_token_accounts

          # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
