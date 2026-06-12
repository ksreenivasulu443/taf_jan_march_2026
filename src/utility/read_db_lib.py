from dotenv import load_dotenv
import os
from src.utility.helpers import read_query
from pyspark.sql import SparkSession
load_dotenv()



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

def read_table(spark,table):
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