import pytest

@pytest.fixture(scope='module')
def read_data(spark_session,read_config):
    pass

# read_sql is needed only when source/target is database
# read_schmea is need only when source/target is file

@pytest.fixture(scope='module')
def read_config():
    pass



@pytest.fixture(scope='session')
def spark_session():
    pass
