from src.utility.report_lib import write_output

def regex_check(df,column,pattern,failure_count=5):

    failed_df=df.filter(
        ~df[column].rlike(pattern)
    )

    failed_count=failed_df.count()

    if failed_count>0:

        failed_preview=[
            row.asDict()
            for row in failed_df.limit(failure_count).collect()
        ]

        status="FAIL"

        write_output(
            "Regex Validation",
            status,
            f"Failed count:{failed_count} Sample:{failed_preview}"
        )

    else:

        status="PASS"

        write_output(
            "Regex Validation",
            status,
            "Regex validation successful"
        )

    return status