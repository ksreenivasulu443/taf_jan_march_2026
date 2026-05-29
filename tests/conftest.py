import pytest
from pyspark.sql import SparkSession
import os
import yaml
from utility.read_file_lib import read_file
from utility.read_db_lib import read_db

@pytest.fixture(scope='module')
def read_data(spark_session,read_config, request):
    # code to read config and create validables for source_config, target_config and validation
    config_data = read_config
    spark = spark_session
    dir_path = request.node.fspath.dirname
    print("=" * 100)
    print("config data", config_data)
    print("=" * 100)
    source_config = config_data['source']
    target_config = config_data['target']

    #Code to read source data
    if source_config['type'] == 'database':
        source_df = read_db(spark=spark,config=source_config, dir_path=dir_path)

    else:
        source_df = read_file(spark = spark,
                              file_type=source_config['type'],
                              file_path=source_config['path'],
                              file_config=source_config['file_config'],
                              dir_path= dir_path)

    #Code to read target data
    if target_config['type'] == 'database':
        target_df = read_db(spark=spark,config=target_config, dir_path=dir_path)

    else:
        target_df = read_file(spark = spark,
                              file_type=target_config['type'],
                              file_path=target_config['path'],
                              file_config=target_config['file_config'],
                              dir_path= dir_path)

    return source_df, target_df

# read_sql is needed only when source/target is database
# read_schmea is need only when source/target is file

@pytest.fixture(scope='module')
def read_config(request):
    print("This is read_config fixture")
    dir_path = request.node.fspath.dirname
    # config_path = dir_path + '/' + 'config.yml'
    print("dir path", dir_path)

    config_path = os.path.join(dir_path, 'config.yml')
    print("config path", config_path)
    with open(config_path, 'r') as f:
        config_data = yaml.safe_load(f)
    return config_data



@pytest.fixture(scope='session')
def spark_session():
    taf_jan = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    jar_path = os.path.join(taf_jan, 'jars', 'mssql-jdbc-12.2.0.jre8.jar')
    print("\n this is start spark session fixture")
    print("taf_jan", taf_jan)
    print("jar_path", jar_path)
    #jar_path = "/Users/admin/PycharmProjects/taf_jan_march_2026/jar/mssql-jdbc-12.2.0.jre8.jar"
    spark = (SparkSession.builder.master('local[1]')
             .config("spark.jars", jar_path)
             .config("spark.driver.extraClassPath", jar_path)
             .config("spark.executor.extraClassPath", jar_path)
             .appName("ETL Automation FW").getOrCreate())
    print("\n this is end of spark session fixture")
    yield spark
    spark.stop()
