from pyspark.sql import SparkSession

def get_spark_session():
    """
    Creates a Spark session for local Glue container.
    Includes MySQL JDBC JAR loaded from S3.
    """
    spark = (
        SparkSession.builder
        .appName("Local-Glue-ETL")
        # Load MySQL JAR from S3 (Option B)
        .config("spark.jars", "s3://<S3_BUCKET_NAME>/libs/mysql-connector-java-8.0.33.jar")
        .config("spark.sql.sources.partitionOverwriteMode", "dynamic")
        .config("spark.hadoop.fs.s3.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        .config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.DefaultAWSCredentialsProviderChain")
        .getOrCreate()
    )
    return spark
