from src.utility.report_lib import write_output

def range_check(df,column,min_value,max_value,failure_count=5):

    failed_df=df.filter(
        f"{column}<{min_value} OR {column}>{max_value}"
    )

    failed_count=failed_df.count()

    if failed_count>0:

        failed_preview=[
            row.asDict()
            for row in failed_df.limit(failure_count).collect()
        ]

        status="FAIL"

        write_output(
            validation_type="Range Check",
            status=status,
            details=f"""
            Column:{column}
            Failed Count:{failed_count}
            Sample:{failed_preview}
            """
        )

    else:

        status="PASS"

        write_output(
            validation_type="Range Check",
            status=status,
            details=f"{column} values within range"
        )

    return status