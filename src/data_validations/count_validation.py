from src.utility.report_lib import write_output
from src.data_validations.records_only_source import records_only_in_source
from src.data_validations.records_only_target import records_only_in_target
def count_check(source_df, target_df, key_columns):
    print("="*50)
    print("Count validation has started....")
    source_cnt = source_df.count()
    target_cnt = target_df.count()

    if source_cnt == target_cnt:
        status = 'PASS'
        write_output(validation_type='count check', status= status, details=f"Count is matching between source and target. Source count is {source_cnt} and target count is {target_cnt}")
        records_only_in_source(source_df=source_df, target_df=target_df, key_columns=key_columns)
        records_only_in_target(source_df=source_df, target_df=target_df, key_columns=key_columns)
    else:
        status = 'FAIL'
        write_output(validation_type='count check', status=status,
                     details=f"""Count is not matching between source and target. "
              Source count is {source_cnt} and target count is {target_cnt} and difference is {source_cnt-target_cnt}""")
        records_only_in_source(source_df=source_df, target_df=target_df, key_columns=key_columns)
        records_only_in_target(source_df=source_df, target_df=target_df, key_columns=key_columns)
    print("Count validation has end....")
    print("=" * 50)
    return status