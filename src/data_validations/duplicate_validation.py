from src.utility.report_lib import write_output

# from pyspark.sql import SparkSession
#
# spark = SparkSession.builder.getOrCreate()
#
# target_df = spark.read.csv('/Users/admin/PycharmProjects/taf_jan_march_2026/input_files/customer_target.csv', header=True)
#
#
# target_df.show()


def duplicate_check(df,primary_key,failure_count=100):
    duplicate_df = df.groupBy(primary_key).count().filter('count>1')
    duplicate_record_count = duplicate_df.count()
    duplicate_df.show()

    if duplicate_record_count == 0:
        status ='PASS'
        write_output(
            "Duplicate check:",
            status,
            f"No Duplicate found!"
        )
    else:
        failed_records = duplicate_df.limit(failure_count).collect()  # Get the first 5 failing rows
        print("failed records", failed_records)
        failed_preview = [row.asDict() for row in failed_records]
        print("failed_preview", failed_preview)  # Convert rows to a dictionary for display
        status = "FAIL"

        write_output(
            "Duplicate check:",
            status,
            f"Duplicate count: {duplicate_record_count} and sample records: {failed_preview}"
        )
    return status