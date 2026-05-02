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
        print("*" * 100)

    return config_data



@pytest.fixture(scope='session')
def spark_session():
    print("\n this is start spark session fixture")
    spark = SparkSession.builder.appName("TAF").getOrCreate()
    print("\n this is end of spark session fixture")
    yield spark
    spark.stop()
