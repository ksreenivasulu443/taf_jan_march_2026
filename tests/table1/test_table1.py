from src.data_validations.count_validation import count_check


def test_count(read_data):
    source_df, target_df = read_data
    print("source df is ")
    print("="*200)
    source_df.show()
    print("target df is ")
    print("=" * 200)
    target_df.show()
    status = count_check(source_df=source_df,target_df=target_df)

    assert status == 'PASS'



