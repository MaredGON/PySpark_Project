import unittest
from pyspark.sql import SparkSession
from src.process import get_product_category_pairs_and_orphan_products

class ProcessTest(unittest.TestCase):

    def setUp(self):
        self.spark = SparkSession.builder.appName("Test").getOrCreate()

        self.products_data = [("Product1",), ("Product2",), ("Product3",), ("Product4",)]
        self.categories_data = [("Category1",), ("Category2",), ("Category3",)]
        self.product_category_rel_data = [("Product1", "Category1"), ("Product1", "Category2"), ("Product2", "Category2")]

        self.products = self.spark.createDataFrame(self.products_data, ["ProductName"])
        self.categories = self.spark.createDataFrame(self.categories_data, ["CategoryName"])
        self.product_category_rel = self.spark.createDataFrame(self.product_category_rel_data, ["ProductName", "CategoryName"])

    def test_get_product_category_pairs_and_orphan_products(self):
        product_category_pairs, orphan_products = get_product_category_pairs_and_orphan_products(
            self.products, self.categories, self.product_category_rel)

        self.assertEqual(product_category_pairs.count(), 3)
        self.assertEqual(orphan_products.count(), 2)

if __name__ == '__main__':
    unittest.main()
