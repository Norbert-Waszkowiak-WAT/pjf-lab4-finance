import unittest
from time import sleep

import keys
from stock_data_analyzer import StockDataAnalyzer


class TestRealStockDataAnalyzer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        sleep(15)
        cls.analyzer = StockDataAnalyzer(keys.api_key, 'AAPL', '2024-01-01', '2024-05-31')

    def test_calculate_average_price(self):
        average_price = self.analyzer.calculate_average_price()
        self.assertIsInstance(average_price, float)

    def test_calculate_max_price(self):
        max_price = self.analyzer.calculate_max_price()
        self.assertIsInstance(max_price, float)

    def test_calculate_min_price(self):
        min_price = self.analyzer.calculate_min_price()
        self.assertIsInstance(min_price, float)

    def test_calculate_volume(self):
        volume = self.analyzer.calculate_volume()
        self.assertIsInstance(volume, float)

    def test_calculate_price_change(self):
        price_change = self.analyzer.calculate_price_change()
        self.assertIsInstance(price_change, float)

    def test_calculate_price_change_percentage(self):
        price_change_percentage = self.analyzer.calculate_price_change_percentage()
        self.assertIsInstance(price_change_percentage, float)


if __name__ == '__main__':
    unittest.main()
