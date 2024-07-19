from pyspark.sql import SparkSession

def load_data(spark, file_path):
    return spark.read.csv(file_path, header=True, inferSchema=True)

def load_products(spark, config):
    return load_data(spark, config.PRODUCTS_FILE)

def load_categories(spark, config):
    return load_data(spark, config.CATEGORIES_FILE)

def load_product_category_rel(spark, config):
    return load_data(spark, config.PRODUCT_CATEGORY_REL_FILE)
