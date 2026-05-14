
from src.utility.report_lib import write_output


# from pyspark.sql import SparkSession
#
# spark = SparkSession.builder.getOrCreate()
#
# df = spark.read.csv("/Users/admin/PycharmProjects/taf_jan_march_2026/input_files/Contact_info.csv", header=True)
#
# df.show()
#
# primary_key = ['Identifier']

def duplicate_check(df, primary_keys):
    """Validate that there are no duplicate rows in the specified columns."""


    duplicates = df.groupBy(primary_keys).count().filter("count > 1")
    #df.createOrReplaceTempView('df')
    #duplicates = spark.sql("select keycol, count(1) from df group by keycol having count(1)>1")

    print("duplcates dataframe")
    duplicates.show()
    duplicate_count = duplicates.count()
    print("duplcates count", duplicate_count)

    if duplicate_count > 0:
        failed_records = duplicates.limit(5).collect()  # Get the first 5 failing rows
        failed_preview = [row.asDict() for row in failed_records]  # Convert rows to a dictionary for display
        status = "FAIL"
        write_output(
            "Duplicate Check",
            status,
            f"Duplicate Count: {duplicate_count}, Sample Failed Records: {failed_preview}"
        )
        return status
    else:
        status = "PASS"
        write_output("Duplicate Check", status, "No duplicates found.")
        return status

#
# duplicate_check(df=df, key_col=primary_key)