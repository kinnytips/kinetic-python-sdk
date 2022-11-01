"""
    @kin-kinetic/api

    The OpenAPI definition of the Kinetic API  # noqa: E501

    The version of the OpenAPI document: 1.0.0-rc.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import kinetic_sdk_generated
from kinetic_sdk_generated.model.app_config_api import AppConfigApi
from kinetic_sdk_generated.model.app_config_app import AppConfigApp
from kinetic_sdk_generated.model.app_config_environment import AppConfigEnvironment
from kinetic_sdk_generated.model.app_config_mint import AppConfigMint
globals()['AppConfigApi'] = AppConfigApi
globals()['AppConfigApp'] = AppConfigApp
globals()['AppConfigEnvironment'] = AppConfigEnvironment
globals()['AppConfigMint'] = AppConfigMint
from kinetic_sdk_generated.model.app_config import AppConfig


class TestAppConfig(unittest.TestCase):
    """AppConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAppConfig(self):
        """Test AppConfig"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AppConfig()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()