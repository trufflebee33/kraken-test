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

from kraken_sdk.models.domain_results_page import DomainResultsPage

class TestDomainResultsPage(unittest.TestCase):
    """DomainResultsPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DomainResultsPage:
        """Test DomainResultsPage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DomainResultsPage`
        """
        model = DomainResultsPage()
        if include_optional:
            return DomainResultsPage(
                items = [
                    kraken_sdk.models.full_domain.FullDomain(
                        uuid = '', 
                        domain = 'example.com', 
                        comment = 'This is a important domain!', 
                        workspace = '', 
                        tags = [
                            kraken_sdk.models.simple_tag.SimpleTag(
                                uuid = '', 
                                name = '', 
                                color = kraken_sdk.models.color.Color(
                                    r = 0, 
                                    g = 0, 
                                    b = 0, 
                                    a = 0, ), 
                                tag_type = 'Workspace', )
                            ], 
                        sources = kraken_sdk.models.simple_aggregation_source.SimpleAggregationSource(
                            bruteforce_subdomains = 0, 
                            tcp_port_scan = 0, 
                            query_certificate_transparency = 0, 
                            query_dehashed = 0, 
                            host_alive = 0, 
                            service_detection = 0, 
                            dns_resolution = 0, 
                            manual = True, ), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                limit = 50,
                offset = 0,
                total = 0
            )
        else:
            return DomainResultsPage(
                items = [
                    kraken_sdk.models.full_domain.FullDomain(
                        uuid = '', 
                        domain = 'example.com', 
                        comment = 'This is a important domain!', 
                        workspace = '', 
                        tags = [
                            kraken_sdk.models.simple_tag.SimpleTag(
                                uuid = '', 
                                name = '', 
                                color = kraken_sdk.models.color.Color(
                                    r = 0, 
                                    g = 0, 
                                    b = 0, 
                                    a = 0, ), 
                                tag_type = 'Workspace', )
                            ], 
                        sources = kraken_sdk.models.simple_aggregation_source.SimpleAggregationSource(
                            bruteforce_subdomains = 0, 
                            tcp_port_scan = 0, 
                            query_certificate_transparency = 0, 
                            query_dehashed = 0, 
                            host_alive = 0, 
                            service_detection = 0, 
                            dns_resolution = 0, 
                            manual = True, ), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                limit = 50,
                offset = 0,
                total = 0,
        )
        """

    def testDomainResultsPage(self):
        """Test DomainResultsPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
