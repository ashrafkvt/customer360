import sys
from etl_package.utils.spark_session import get_spark_session
from etl_package.utils.db_connector import write_to_mysql
from etl_package.config.constants import CUSTOMER_FILE, DATE_FILE, TRANSACTION_FILE
from etl_package.transformations.customer_transform import transform_customer
from etl_package.transformations.date_transform import transform_date
from etl_package.transformations.transaction_transform import transform_transaction

def main():
    spark = get_spark_session()

    # --- Load CSVs from S3 ---
    df_customer = spark.read.option("header", "true").csv(CUSTOMER_FILE)
    df_date = spark.read.option("header", "true").csv(DATE_FILE)
    df_transaction = spark.read.option("header", "true").csv(TRANSACTION_FILE)

    # --- Apply simple transformations ---
    df_customer_transformed = transform_customer(df_customer)
    df_date_transformed = transform_date(df_date)
    df_transaction_transformed = transform_transaction(df_transaction)

    # --- Write to local MySQL ---
    write_to_mysql(df_customer_transformed, "dim_customer")
    write_to_mysql(df_date_transformed, "dim_date")
    write_to_mysql(df_transaction_transformed, "fact_transaction")

    print("ETL job completed successfully!")

if __name__ == "__main__":
    main()
