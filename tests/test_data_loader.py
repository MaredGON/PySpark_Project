import unittest
from pyspark.sql import SparkSession
from src.data_loader import load_products, load_categories, load_product_category_rel
from src.config import Config

class DataLoaderTest(unittest.TestCase):

    def setUp(self):
        self.spark = SparkSession.builder.appName("Test").getOrCreate()
        self.config = Config()

    def test_load_products(self):
        df = load_products(self.spark, self.config)
        self.assertIsNotNone(df)
        self.assertGreater(df.count(), 0)

    def test_load_categories(self):
        df = load_categories(self.spark, self.config)
        self.assertIsNotNone(df)
        self.assertGreater(df.count(), 0)

    def test_load_product_category_rel(self):
        df = load_product_category_rel(self.spark, self.config)
        self.assertIsNotNone(df)
        self.assertGreater(df.count(), 0)

if __name__ == '__main__':
    unittest.main()
