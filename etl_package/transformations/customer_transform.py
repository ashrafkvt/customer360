from pyspark.sql.functions import upper, col

def transform_customer(df):
    return df.withColumn("customer_name", upper(col("customer_name")))
