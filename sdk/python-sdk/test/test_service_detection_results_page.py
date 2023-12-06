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

from kraken_sdk.models.service_detection_results_page import ServiceDetectionResultsPage

class TestServiceDetectionResultsPage(unittest.TestCase):
    """ServiceDetectionResultsPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDetectionResultsPage:
        """Test ServiceDetectionResultsPage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDetectionResultsPage`
        """
        model = ServiceDetectionResultsPage()
        if include_optional:
            return ServiceDetectionResultsPage(
                items = [
                    kraken_sdk.models.full_service_detection_result.FullServiceDetectionResult(
                        uuid = '', 
                        attack = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        certainty = 'Historical', 
                        service_names = [
                            ''
                            ], 
                        host = '127.0.0.1', 
                        port = 56, )
                    ],
                limit = 50,
                offset = 0,
                total = 0
            )
        else:
            return ServiceDetectionResultsPage(
                items = [
                    kraken_sdk.models.full_service_detection_result.FullServiceDetectionResult(
                        uuid = '', 
                        attack = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        certainty = 'Historical', 
                        service_names = [
                            ''
                            ], 
                        host = '127.0.0.1', 
                        port = 56, )
                    ],
                limit = 50,
                offset = 0,
                total = 0,
        )
        """

    def testServiceDetectionResultsPage(self):
        """Test ServiceDetectionResultsPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
