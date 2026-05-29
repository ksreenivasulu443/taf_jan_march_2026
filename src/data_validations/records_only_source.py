from utility.report_lib import write_output


# from pyspark.sql import SparkSession
#
# spark = SparkSession.builder.getOrCreate()
#
# source_df = spark.read.csv('/Users/admin/PycharmProjects/taf_jan_march_2026/input_files/customer_source.csv', header=True)
#
# target_df = spark.read.csv('/Users/admin/PycharmProjects/taf_jan_march_2026/input_files/customer_target.csv', header=True)
#
# source_df.show()
# target_df.show()

def records_only_in_source(source_df, target_df, key_columns,failure_count=5):
    """Validate records present only in the source."""
    only_in_source = source_df.select(key_columns).exceptAll(target_df.select(key_columns))
    only_in_source.show()
    count_only_in_source = only_in_source.count()
    if count_only_in_source > 0:
        failed_records = only_in_source.limit(failure_count).collect() # Get the first 5 failing rows
        print("failed records",failed_records)
        failed_preview = [row.asDict() for row in failed_records]
        print("failed_preview", failed_preview)# Convert rows to a dictionary for display
        status = "FAIL"
        write_output(
            "Records Only in Source",
            status,
            f"Count: {count_only_in_source}, Sample Failed Records: {failed_preview}"
        )

    else:
        status = "PASS"
        write_output("Records Only in Source", status, "No extra records found in source.")

    return status


# records_only_in_source(source_df=source_df, target_df=target_df, key_columns=['customer_id'], failure_count=5)
#




















