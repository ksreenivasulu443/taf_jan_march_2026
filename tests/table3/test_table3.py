from src.data_validations.count_validation import count_check
from src.data_validations.records_only_source import records_only_in_source
from src.data_validations.records_only_target import records_only_in_target
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


#
# def test_duplicate(read_data):
#     source_df, target_df = read_data
#     print("source_df is")
#     source_df.show()
#     print("target_df is")
#     target_df.show()
#     dup = target_df.groupBy('customer_id').count().filter('count>1')
#     assert dup.count() == 0