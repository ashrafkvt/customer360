from pyspark.sql.functions import col

def transform_transaction(df):
    return df \
        .withColumn("amount", col("amount").cast("double")) \
        .withColumn("quantity", col("quantity").cast("int"))
