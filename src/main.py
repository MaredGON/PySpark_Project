from pyspark.sql import SparkSession
from config import Config
from data_loader import load_products, load_categories, load_product_category_rel
from process import get_product_category_pairs_and_orphan_products

def main():
    spark = SparkSession.builder.appName("ProductCategoryExample").getOrCreate()
    config = Config()

    products = load_products(spark, config)
    categories = load_categories(spark, config)
    product_category_rel = load_product_category_rel(spark, config)

    product_category_pairs, orphan_products = get_product_category_pairs_and_orphan_products(products, categories, product_category_rel)

    product_category_pairs.show()
    orphan_products.show()

if __name__ == "__main__":
    main()
