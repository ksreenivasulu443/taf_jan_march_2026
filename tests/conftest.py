import pytest
from pyspark.sql import SparkSession
import os
import yaml

@pytest.fixture(scope='module')
def read_data(spark_session,read_config):
    return 'source'

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
        print("*"*100)
        print("conif data", config_data)
        print("type of config data", type(config_data))
        print("source config", config_data['source'])
        print("target config", config_data['target'])
        print("validation config", config_data['validation'])

        print("source config path", config_data['source']['path'])
        print("source config type", config_data['source']['type'])
        print("source config schema", config_data['source']['schema'])

        print("target config path", config_data['target']['path'])
        print("target config type", config_data['target']['type'])
        print("target config schema", config_data['target']['schema'])
        print("*" * 100)

    return config_data



@pytest.fixture(scope='session')
def spark_session():
    print("\n this is start spark session fixture")
    spark = SparkSession.builder.appName("TAF").getOrCreate()
    print("\n this is end of spark session fixture")
    yield spark
    spark.stop()
