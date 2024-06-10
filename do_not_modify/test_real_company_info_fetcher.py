import unittest
from time import sleep

import keys
from company_info_fetcher import CompanyInfoFetcher


class TestCompanyInfoFetcher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sleep(5)
        cls.fetcher = CompanyInfoFetcher(keys.api_key, 'AAPL')

    def test_get_company_name(self):
        company_name = self.fetcher.get_company_name()
        self.assertIsInstance(company_name, str)

    def test_get_locale(self):
        ceo = self.fetcher.get_locale()
        self.assertIsInstance(ceo, str)

    def test_get_sic_code(self):
        sector = self.fetcher.get_sic_code()
        self.assertIsInstance(sector, str)

    def test_get_description(self):
        description = self.fetcher.get_description()
        self.assertIsInstance(description, str)


if __name__ == '__main__':
    unittest.main()
