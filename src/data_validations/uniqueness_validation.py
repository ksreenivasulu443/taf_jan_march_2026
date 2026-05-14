from src.utility.report_lib import write_output

# from pyspark.sql import SparkSession
#
# spark = SparkSession.builder.getOrCreate()
#
# df = spark.read.csv("/Users/admin/PycharmProjects/taf_jan_march_2026/input_files/Contact_info.csv", header=True)
#
# df.show()
#
# unique_cols = ['Identifier', 'Surname','birthmonth']

def uniqueness_check(df, unique_cols):
    """Validate that specified columns have unique values."""
    duplicate_counts = {}  #  {'Identifier':2,'Surname':3,'birthmonth':3 }
    for column in unique_cols:
        dup_df = df.groupBy(column).count().filter("count > 1")
        dup_df.show()
        count_duplicates = dup_df.count()
        print("count_duplicates", column, count_duplicates)
        duplicate_counts[column] = count_duplicates

    print("duplicate_counts", duplicate_counts)

    status = "PASS" if all(count == 0 for count in duplicate_counts.values()) else "FAIL"
    write_output(
        "Uniqueness Check",
        status,
        f"Duplicate counts per column: {duplicate_counts}"
    )
    return status


# uniqueness_check(df=df, unique_cols=unique_cols)