"""
    @kin-kinetic/api

    The OpenAPI definition of the Kinetic API  # noqa: E501

    The version of the OpenAPI document: 1.0.0-rc.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import kinetic_sdk_generated
from kinetic_sdk_generated.model.confirmed_transaction_meta import ConfirmedTransactionMeta
from kinetic_sdk_generated.model.transaction_data import TransactionData
globals()['ConfirmedTransactionMeta'] = ConfirmedTransactionMeta
globals()['TransactionData'] = TransactionData
from kinetic_sdk_generated.model.transaction_response import TransactionResponse


class TestTransactionResponse(unittest.TestCase):
    """TransactionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransactionResponse(self):
        """Test TransactionResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TransactionResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()