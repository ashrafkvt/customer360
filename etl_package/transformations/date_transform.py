from pyspark.sql.functions import to_date, col

def transform_date(df):
    return df.withColumn("date", to_date(col("date")))
