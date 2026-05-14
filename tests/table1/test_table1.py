from src.data_validations.count_validation import count_check
from src.data_validations.duplicate_validation import duplicate_check
from src.data_validations.uniqueness_validation import uniqueness_check
from src.data_validations.null_value_validation import null_value_check
from src.data_validations.schema_validation import schema_check


def test_count_check(read_data,read_config):
    source_df, target_df = read_data
    config = read_config
    key_columns = config['validation']['key_columns']
    status = count_check(source_df=source_df,target_df=target_df,key_columns=key_columns)
    assert status == 'PASS'


def test_duplicate_check(read_data,read_config):
    _, target_df = read_data
    config = read_config
    primary_keys = config['validation']['primary_key_columns']
    status = duplicate_check(df=target_df, primary_keys=primary_keys)
    assert status == 'PASS'

def test_uniqueness_check(read_data,read_config):
    source_df, target_df = read_data
    config = read_config
    unique_columns = config['validation']['unique_columns']
    status = uniqueness_check(df=target_df, unique_cols=unique_columns)
    assert status == 'PASS'


def test_null_check(read_data,read_config):
    source_df, target_df = read_data
    config = read_config
    not_null_columns = config['validation']['not_null_columns']
    status = null_value_check(df=target_df, not_null_columns=not_null_columns)
    assert status == 'PASS'

def test_schema_check(read_data, spark_session):
    source_df, target_df = read_data
    spark = spark_session
    status = schema_check(source_df, target_df, spark)
    assert status == 'PASS'


