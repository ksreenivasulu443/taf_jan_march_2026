from src.utility.report_lib import write_output
def count_check(source_df, target_df):
    print("="*50)
    print("Count validation has started....")
    source_cnt = source_df.count()
    target_cnt = target_df.count()

    if source_cnt == target_cnt:
        status = 'PASS'
        write_output(validation_type='count check', status= status, details=f"Count is matching between source and target. Source count is {source_cnt} and target count is {target_cnt}")
    else:
        status = 'FAIL'
        write_output(validation_type='count check', status=status,
                     details=f"""Count is not matching between source and target. "
              Source count is {source_cnt} and target count is {target_cnt} and difference is {source_cnt-target_cnt}""")

    print("Count validation has end....")
    print("=" * 50)
    return status