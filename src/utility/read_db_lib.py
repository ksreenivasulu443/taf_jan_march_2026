from dotenv import load_dotenv
import os
from src.utility.helpers import read_query
from pyspark.sql import SparkSession
load_dotenv()

jar_path= "/Users/admin/PycharmProjects/taf_jan_march_2026/jars/mssql-jdbc-12.2.0.jre8.jar"


spark = (SparkSession.builder.master('local[1]')
             .config("spark.jars", jar_path)
             .config("spark.driver.extraClassPath", jar_path)
             .config("spark.executor.extraClassPath", jar_path)
             .appName("ETL Automation FW").getOrCreate())

def read_db(spark,config, dir_path):
    if config['transformation'][0].upper() == 'Y' and config['transformation'][1].upper()=='SQL':
        query = read_query(dir_path)

        print("query", query)

        df = spark.read.format("jdbc") \
            .option("url",os.getenv("URL")) \
            .option("user", os.getenv("USER_NAME")) \
            .option("password", os.getenv("DB_PASSWORD")) \
            .option("query", query) \
            .option("driver", os.getenv("DRIVER_CLASS")) \
            .load()
    else:
        df = spark.read.format("jdbc") \
            .option("url",os.getenv("URL")) \
            .option("user", os.getenv("USER_NAME")) \
            .option("password", os.getenv("DB_PASSWORD")) \
            .option("dbtable", config['table']) \
            .option("driver", os.getenv("DRIVER_CLASS")) \
            .load()

    return df

def read_table(table):
    df = spark.read.format("jdbc") \
            .option("url",os.getenv("URL")) \
            .option("user", os.getenv("USER_NAME")) \
            .option("password", os.getenv("DB_PASSWORD")) \
            .option("dbtable", table) \
            .option("driver", os.getenv("DRIVER_CLASS")) \
            .load()

    return df

def df_write(df, expected_table):
    jdbc_properties = {
        "user": os.getenv("USER_NAME"),
        "password": os.getenv("DB_PASSWORD"),
        "driver": os.getenv("DRIVER_CLASS")
    }

    df.write.jdbc(url=os.getenv("URL"), table=expected_table, mode="overwrite", properties=jdbc_properties)