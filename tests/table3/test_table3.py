from src.data_validations.count_validation import count_check
from src.data_validations.records_only_source import records_only_in_source
from src.data_validations.records_only_target import records_only_in_target
from src.data_validations.duplicate_validation import duplicate_check
from src.data_validations.uniqueness_validation import uniqueness_check
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
#
# def test_record_only_source(read_data, read_config):
#     source_df, target_df = read_data
#     config = read_config
#     print("source_df is")
#     source_df.show()
#     print("target_df is")
#     target_df.show()
#     key_columns = config['validation']['key_columns']
#     status = records_only_in_source(source_df=source_df, target_df=target_df, key_columns=key_columns)
#     assert status == 'PASS'
#
# def test_record_only_target(read_data, read_config):
#     source_df, target_df = read_data
#     config = read_config
#     print("source_df is")
#     source_df.show()
#     print("target_df is")
#     target_df.show()
#     key_columns = config['validation']['key_columns']
#     status = records_only_in_target(source_df=source_df, target_df=target_df, key_columns=key_columns)
#     assert status == 'PASS'



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