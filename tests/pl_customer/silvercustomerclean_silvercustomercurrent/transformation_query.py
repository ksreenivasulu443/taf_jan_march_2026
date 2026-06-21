from src.utility.read_db_lib import (
    read_table,
    df_write
)


def run_transformation(
        spark,
        source_config,
        target_config):

    silver_current_backup = read_table(
        spark,
        '[silver].[Customer_Current_Backup]'
    )

    silver_clean = read_table(
        spark,
        '[silver].[Customer_Clean]'
    )

    silver_clean = silver_clean.filter(
        "SourceFileName='customer_28052026.csv'"
    )

    columns = silver_clean.columns

    new_records = silver_clean.join(
        silver_current_backup,
        on='CustomerID',
        how='left_anti'
    )

    update_records = silver_clean.join(
        silver_current_backup.select('CustomerID'),
        on='CustomerID',
        how='inner'
    )

    not_received = silver_current_backup.join(
        silver_clean,
        on='CustomerID',
        how='left_anti'
    )

    final_df = (
        new_records.select(*columns)
        .union(update_records.select(*columns))
        .union(not_received.select(*columns))
    )

    print("Final Data")

    final_df.show()

    df_write(
        df=final_df,
        expected_table='[silver].[Customer_Current_expected]'
    )