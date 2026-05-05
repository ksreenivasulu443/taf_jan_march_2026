from pyspark.sql import SparkSession

from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("DB_PASSWORD"))

jar_path = "/Users/admin/PycharmProjects/taf_august/jars/mssql-jdbc-12.2.0.jre8.jar"

spark = (SparkSession.builder.master('local[1]')
             .config("spark.jars", jar_path)
             .config("spark.driver.extraClassPath", jar_path)
             .config("spark.executor.extraClassPath", jar_path)
             .appName("ETL Automation FW").getOrCreate())


df_sql_server = spark.read.format("jdbc") \
    .option("url", "jdbc:sqlserver://autoadminfeb.database.windows.net:1433;database=test_db;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30;") \
    .option("user", os.getenv("USER_NAME")) \
    .option("password", os.getenv("DB_PASSWORD")) \
    .option("dbtable", "dbo.Customers") \
    .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
    .load()

df_sql_server.show()
