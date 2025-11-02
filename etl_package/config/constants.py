S3_BUCKET = "<S3_BUCKET_NAME>"
S3_FOLDER = "<S3_FOLDER_PATH>"

CUSTOMER_FILE = f"s3://{S3_BUCKET}/{S3_FOLDER}/dim_customer.csv"
DATE_FILE = f"s3://{S3_BUCKET}/{S3_FOLDER}/dim_date.csv"
TRANSACTION_FILE = f"s3://{S3_BUCKET}/{S3_FOLDER}/fact_transaction.csv"

# MySQL table names
CUSTOMER_TABLE = "dim_customer"
DATE_TABLE = "dim_date"
TRANSACTION_TABLE = "fact_transaction"
