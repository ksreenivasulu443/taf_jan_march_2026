import pytest
from pyspark.sql import SparkSession
import os
import yaml
from src.utility.read_file_lib import read_file
from src.utility.read_db_lib import read_db

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
    validation_config = config_data['validation']
    #Code to read source data
    if source_config['type'] == 'database':
        source_df = read_db(spark = spark,config=source_config,dir_path=dir_path)
    else:
        source_df = read_file(spark = spark,
                              file_type=source_config['type'],
                              file_path=source_config['path'],
                              file_config=source_config['file_config'],
                              dir_path= dir_path)

    #Code to read target data
    if target_config['type'] == 'database':
        target_df = read_db(spark=spark,config=target_config,dir_path=dir_path)
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
        #print("*"*100)
        # print("conif data", config_data)
        # print("type of config data", type(config_data))
        # print("source config", config_data['source'])
        # print("target config", config_data['target'])
        # print("validation config", config_data['validation'])
        #
        # print("source config path", config_data['source']['path'])
        # print("source config type", config_data['source']['type'])
        # print("source config schema", config_data['source']['schema'])
        #
        # print("target config path", config_data['target']['path'])
        # print("target config type", config_data['target']['type'])
        # print("target config schema", config_data['target']['schema'])
        # print("*" * 100)

    return config_data



@pytest.fixture(scope='session')
def spark_session():
    print("\n this is start spark session fixture")
    jar_path = "/Users/admin/PycharmProjects/taf_jan_march_2026/jar/mssql-jdbc-12.2.0.jre8.jar"
    spark = (SparkSession.builder.master('local[1]')
             .config("spark.jars", jar_path)
             .config("spark.driver.extraClassPath", jar_path)
             .config("spark.executor.extraClassPath", jar_path)
             .appName("ETL Automation FW").getOrCreate())
    print("\n this is end of spark session fixture")
    yield spark
    spark.stop()
