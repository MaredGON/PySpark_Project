from pyspark.sql.functions import col

def get_product_category_pairs_and_orphan_products(products, categories, product_category_rel):
    product_category_pairs = products.join(product_category_rel, "ProductName", "left") \
                                     .join(categories, "CategoryName", "left") \
                                     .select("ProductName", "CategoryName")

    orphan_products = product_category_pairs.filter(col("CategoryName").isNull()).select("ProductName").distinct()

    return product_category_pairs, orphan_products
