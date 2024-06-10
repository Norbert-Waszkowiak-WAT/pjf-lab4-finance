import unittest
from unittest.mock import patch, MagicMock

from company_info_fetcher import CompanyInfoFetcher


class TestMockedCompanyInfoFetcher(unittest.TestCase):
    @patch('requests.get')
    def setUp(self, mock_get):
        # Mock the API response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "request_id": "17f6061f721fb6cc5711e415220c305b",
            "results": {
                "ticker": "AAPL",
                "name": "Apple Inc.",
                "market": "stocks",
                "locale": "us",
                "primary_exchange": "XNAS",
                "type": "CS",
                "active": True,
                "currency_name": "usd",
                "cik": "0000320193",
                "composite_figi": "BBG000B9XRY4",
                "share_class_figi": "BBG001S5N8V8",
                "market_cap": 3019127404980,
                "phone_number": "(408) 996-1010",
                "address": {
                    "address1": "ONE APPLE PARK WAY",
                    "city": "CUPERTINO",
                    "state": "CA",
                    "postal_code": "95014"
                },
                "description": "Apple is among the largest companies in the world, with a broad portfolio of hardware and software products targeted at consumers and businesses. Apple's iPhone makes up a majority of the firm sales, and Apple's other products like Mac, iPad, and Watch are designed around the iPhone as the focal point of an expansive software ecosystem. Apple has progressively worked to add new applications, like streaming video, subscription bundles, and augmented reality. The firm designs its own software and semiconductors while working with subcontractors like Foxconn and TSMC to build its products and chips. Slightly less than half of Apple's sales come directly through its flagship stores, with a majority of sales coming indirectly through partnerships and distribution.",
                "sic_code": "3571",
                "sic_description": "ELECTRONIC COMPUTERS",
                "ticker_root": "AAPL",
                "homepage_url": "https://www.apple.com",
                "total_employees": 161000,
                "list_date": "1980-12-12",
                "branding": {
                    "logo_url": "https://api.polygon.io/v1/reference/company-branding/YXBwbGUuY29t/images/2024-06-01_logo.svg",
                    "icon_url": "https://api.polygon.io/v1/reference/company-branding/YXBwbGUuY29t/images/2024-06-01_icon.jpeg"
                },
                "share_class_shares_outstanding": 15334080000,
                "weighted_shares_outstanding": 15334082000,
                "round_lot": 100
            },
            "status": "OK"
        }
        mock_get.return_value = mock_response

        self.fetcher = CompanyInfoFetcher('test_api_key', 'test_ticker')

    def test_get_company_name(self):
        self.assertEqual(self.fetcher.get_company_name(), 'Apple Inc.')

    def test_get_locale(self):
        self.assertEqual(self.fetcher.get_locale(), 'us')

    def test_get_sic_code(self):
        self.assertEqual(self.fetcher.get_sic_code(), '3571')

    def test_get_description(self):
        self.assertEqual(self.fetcher.get_description(), "Apple is among the largest companies in the world, with a broad portfolio of hardware and software products targeted at consumers and businesses. Apple's iPhone makes up a majority of the firm sales, and Apple's other products like Mac, iPad, and Watch are designed around the iPhone as the focal point of an expansive software ecosystem. Apple has progressively worked to add new applications, like streaming video, subscription bundles, and augmented reality. The firm designs its own software and semiconductors while working with subcontractors like Foxconn and TSMC to build its products and chips. Slightly less than half of Apple's sales come directly through its flagship stores, with a majority of sales coming indirectly through partnerships and distribution.")


if __name__ == '__main__':
    unittest.main()
