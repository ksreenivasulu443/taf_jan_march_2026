from src.data_validations.count_validation import count_check


def test_count(read_data,read_config):
    source_df, target_df = read_data
    config = read_config
    print("source df is ")
    print("="*200)
    source_df.show()
    print("target df is ")
    print("=" * 200)
    target_df.show()
    key_columns = config['validation']['key_columns']
    status = count_check(source_df=source_df,target_df=target_df,key_columns=key_columns)

    assert status == 'PASS'



