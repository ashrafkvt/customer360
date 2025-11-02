def write_to_mysql(df, table_name, mode="overwrite"):
    jdbc_url = "jdbc:mysql://local-mysql:3306/<LOCAL_DB_NAME>"
    properties = {
        "user": "<LOCAL_DB_USER>",
        "password": "<LOCAL_DB_PASSWORD>",
        "driver": "com.mysql.cj.jdbc.Driver"
    }

    df.write.jdbc(url=jdbc_url, table=table_name, mode=mode, properties=properties)
