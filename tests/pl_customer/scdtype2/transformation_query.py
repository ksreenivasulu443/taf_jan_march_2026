from src.utility.read_db_lib import (
    read_table,
    df_write
)

from pyspark.sql.functions import current_timestamp,lit


def run_transformation(
        spark,
        source_config,
        target_config):

    silver_History_backup = read_table(
        spark,
        '[silver].[Customer_History_Backup]'
    )

    print("history")

    silver_History_backup.show()
    silver_History_backup_active = silver_History_backup.filter("IsCurrent=true")
    silver_History_backup_inactive = silver_History_backup.filter("IsCurrent=False")

    silver_clean = read_table(
        spark,
        '[silver].[Customer_Clean]'
    )

    print('silver_clean')
    silver_clean.show()
    #
    silver_clean = silver_clean.filter(
        "SourceFileName='customer_13062026.csv'"
    )

    # columns = silver_clean.columns

    new_records = (silver_clean.join(
        silver_History_backup,
        on='CustomerID',
        how='left_anti'
    ).withColumn('EffectiveStartDate', current_timestamp()).withColumn('EffectiveEndDate',lit('2099-12-31T23:59:59'))
                   .withColumn('IsCurrent',lit(True)))

    print("new_records")
    new_records.show()


    present_in_back_not_in_silver = silver_History_backup.join(silver_clean,on='CustomerID',how='left_anti')

    update_new_insert =  (silver_clean.join(
        silver_History_backup,
        on='CustomerID',
        how='left_semi'
    ).withColumn('EffectiveStartDate', current_timestamp()).withColumn('EffectiveEndDate',lit('2099-12-31T23:59:59'))
                         .withColumn('IsCurrent',lit(True)))

    update_mark_history =  (silver_History_backup.join(
        silver_clean,
        on='CustomerID',
        how='left_semi'
    ).withColumn('EffectiveEndDate',lit('2099-12-31T23:59:59')).withColumn('IsCurrent',lit(False)))

    columns = ['CustomerID','CustomerName','Email','PhoneNumber','City','StateName','EffectiveStartDate','EffectiveEndDate','IsCurrent']

    final_df = (new_records.select(*columns).union(present_in_back_not_in_silver.select(*columns)).
            union(update_new_insert.select(*columns)).union(update_mark_history.select(*columns)))


    final_df.show()
    df_write(
        df=final_df,
        expected_table='[silver].[Customer_History_expected]'
    )




