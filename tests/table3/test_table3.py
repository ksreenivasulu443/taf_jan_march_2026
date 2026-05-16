
def test_count(read_data):
    source_df, target_df = read_data
    print("source_df is")
    source_df.show()
    print("target_df is")
    target_df.show()
    assert source_df.count() == target_df.count()

def test_duplicate(read_data):
    source_df, target_df = read_data
    print("source_df is")
    source_df.show()
    print("target_df is")
    target_df.show()
    dup = target_df.groupBy('customer_id').count().filter('count>1')
    assert dup.count() == 0