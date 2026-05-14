from src.utility.report_lib import write_output


def null_value_check(df, not_null_columns,num_records = 5):
    """Validate that specified columns have no null or empty values."""

    failures = []

    for column in not_null_columns: #['customer_id','name','email']
        print("column", column)
        #failing_rows = df.filter((col(column).isNull()) | (trim(col(column)) == "" ))
        failing_rows = df.filter(f"""{column} is null or trim({column}) ='' 
                                   or upper({column}) in ('NA','NULL','NONE','N/A', 'NU') """)

        null_count = failing_rows.count()
        print("null_count", null_count)
        if null_count > 0:
            failed_records = failing_rows.limit(num_records).collect()  # Get the first 5 failing rows
            #print("failed_records", failed_records)
            failed_preview = [row.asDict() for row in failed_records]  # Convert rows to a dictionary for display
            #print("failed preview", failed_preview)
            failures.append({
                "column": column,
                "null_count": null_count,
                "sample_failed_records": failed_preview
            })
            print("failures", failures)

    if len(failures)>0:
        status = "FAIL"
        write_output("Null Value Check", status, f"Failures: {failures}")
        return status
    else:
        status = "PASS"
        write_output("Null Value Check", status, "No null values found.")
        return status

