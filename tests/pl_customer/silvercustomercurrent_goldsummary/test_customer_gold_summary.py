from src.data_validations.count_validation import count_check
from src.data_validations.records_only_source import records_only_in_source
from src.data_validations.records_only_target import records_only_in_target
from src.data_validations.duplicate_validation import duplicate_check
from src.data_validations.uniqueness_validation import uniqueness_check
from src.data_validations.data_compare_validation import data_compare
from src.data_validations.null_value_validation import null_value_check
from src.data_validations.schema_validation import schema_check
from src.dqe.pattern_validation import regex_check
from src.dqe.range_validation import range_check

def test_count(read_data, read_config):
    source_df, target_df = read_data
    config = read_config
    print("source_df is")
    source_df.show()
    print("target_df is")
    target_df.show()
    key_columns = config['validation']['key_columns']
    status = count_check(source_df=source_df, target_df=target_df, key_columns=key_columns)
    assert status == 'PASS'

def test_record_only_source(read_data, read_config):
    source_df, target_df = read_data
    config = read_config
    print("source_df is")
    source_df.show()
    print("target_df is")
    target_df.show()
    key_columns = config['validation']['key_columns']
    status = records_only_in_source(source_df=source_df, target_df=target_df, key_columns=key_columns)
    assert status == 'PASS'

def test_record_only_target(read_data, read_config):
    source_df, target_df = read_data
    config = read_config
    print("source_df is")
    source_df.show()
    print("target_df is")
    target_df.show()
    key_columns = config['validation']['key_columns']
    status = records_only_in_target(source_df=source_df, target_df=target_df, key_columns=key_columns)
    assert status == 'PASS'



def test_duplicate_check(read_data, read_config):
    _, target_df = read_data
    config_data = read_config
    primary_key = config_data['validation']['primary_keys']
    status = duplicate_check(df=target_df, primary_key=primary_key)
    assert status == 'PASS'

def test_uniqueness_check(read_data, read_config):
    _, target_df = read_data
    config_data = read_config
    unique_cols = config_data['validation']['unique_cols']
    status = uniqueness_check(df=target_df, unique_cols=unique_cols)
    assert status == 'PASS'

def test_data_compare(read_data, read_config):
    source_df, target_df = read_data
    config_data = read_config
    key_columns = config_data['validation']['key_columns']
    status = data_compare(source_df = source_df, target_df=target_df, key_columns=key_columns)
    assert status == 'PASS'

def test_null_check(read_data, read_config):
    source_df, target_df = read_data
    config_data = read_config
    not_null_cols = config_data['validation']['not_null_cols']
    status = null_value_check(df = target_df, not_null_columns=not_null_cols)
    assert status == 'PASS'


def test_schema_check(read_data, spark_session):
    source_df, target_df = read_data
    spark = spark_session
    status = schema_check(source=source_df, target=target_df, spark=spark)
    assert status == 'PASS'
#
# def test_name_regex(read_data, spark_session, read_config):
#     source_df, target_df = read_data
#     spark = spark_session
#     config = read_config
#     regex_pattern_col = config['validation']['regex_pattern_col'][0]
#     regex_pattern = config['validation']['regex_pattern_col'][1]
#     status = regex_check(df=target_df,column= regex_pattern_col,pattern=regex_pattern,failure_count=5)
#     assert status == 'PASS'
#
# def test_range_check(read_data, spark_session, read_config):
#     source_df, target_df = read_data
#     spark = spark_session
#     config = read_config
#     range_col = config['validation']['range_col'][0]
#     min_value = config['validation']['range_col'][1]
#     max_value = config['validation']['range_col'][2]
#     status = range_check(df=target_df,column=range,min_value=min_value,max_value=max_value,failure_count=5)
#     assert status == 'PASS'

















# We will resume the session at 11.30 am IST






