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

from kraken_sdk.models.simple_aggregation_source import SimpleAggregationSource

class TestSimpleAggregationSource(unittest.TestCase):
    """SimpleAggregationSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimpleAggregationSource:
        """Test SimpleAggregationSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimpleAggregationSource`
        """
        model = SimpleAggregationSource()
        if include_optional:
            return SimpleAggregationSource(
                bruteforce_subdomains = 0,
                tcp_port_scan = 0,
                query_certificate_transparency = 0,
                query_dehashed = 0,
                host_alive = 0,
                service_detection = 0,
                dns_resolution = 0,
                manual = True
            )
        else:
            return SimpleAggregationSource(
                bruteforce_subdomains = 0,
                tcp_port_scan = 0,
                query_certificate_transparency = 0,
                query_dehashed = 0,
                host_alive = 0,
                service_detection = 0,
                dns_resolution = 0,
                manual = True,
        )
        """

    def testSimpleAggregationSource(self):
        """Test SimpleAggregationSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
