from utility.report_lib import write_output

from data_validations.records_only_source import records_only_in_source
from data_validations.records_only_target import records_only_in_target

def count_check(source_df, target_df, key_columns):

    src_cnt = source_df.count()
    tgt_cnt = target_df.count()
    list_row = source_df.collect()

    if src_cnt == tgt_cnt:
        status = 'PASS'
        write_output(validation_type="count check",
                     status=status,
                     details=f"Count is matching.Source count is {src_cnt} and target count is {tgt_cnt}" )
        records_only_in_source(source_df, target_df, key_columns,failure_count=10)
        records_only_in_target(source_df, target_df, key_columns,failure_count=10)
    else:

        status= 'FAIL'
        write_output(validation_type="count check",
                     status=status,
                     details=f"""Count is not matching.Source count is {src_cnt} and target count is {tgt_cnt}
                             difference is {abs(src_cnt-tgt_cnt)}""")

        records_only_in_source(source_df, target_df, key_columns,failure_count=10)
        records_only_in_target(source_df, target_df, key_columns,failure_count=10)

    return status

