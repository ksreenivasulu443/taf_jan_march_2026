from pyspark.sql.functions import col
from src.utility.report_lib import write_output


def zipcode_validation(
        df,
        column,
        regex_pattern="^[0-9]{6}$",
        failure_count=5):

    """
    Validates zipcode values

    Example:
        zipcode_validation(
            df=df,
            column="zipcode"
        )

    Default:
        Indian ZIP/PIN code (6 digits)

    US Example:
        regex_pattern="^[0-9]{5}(-[0-9]{4})?$"
    """

    failed_df = df.filter(
        (col(column).isNull()) |
        (~col(column).rlike(regex_pattern))
    )

    failed_count = failed_df.count()

    if failed_count > 0:

        failed_preview = [
            row.asDict()
            for row in failed_df.limit(failure_count).collect()
        ]

        status = "FAIL"

        write_output(
            validation_type="Zipcode Validation",
            status=status,
            details=f"""
            Column: {column}
            Failed Count: {failed_count}
            Sample Failed Records:
            {failed_preview}
            """
        )

    else:

        status = "PASS"

        write_output(
            validation_type="Zipcode Validation",
            status="PASS",
            details=f"All zipcode values are valid in column {column}"
        )

    return status