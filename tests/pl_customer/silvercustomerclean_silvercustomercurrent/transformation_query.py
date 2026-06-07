from src.utility.read_db_lib import read_table, df_write

silver_current_backup = read_table(table='[silver].[Customer_Current_Backup]')
silver_current_backup.show()
silver_clean = read_table(table='[silver].[Customer_Clean]')
silver_clean = silver_clean.filter("SourceFileName='customer_28052026.csv' " )
silver_clean.show()

columns = silver_clean.columns

new_records = silver_clean.join(silver_current_backup, on ='CustomerID', how='left_anti')
# new_records.show()
update_records = silver_clean.join(silver_current_backup.select('CustomerID'), on ='CustomerID', how='inner')
not_received = silver_current_backup.join(silver_clean, on='CustomerID', how='left_anti')
not_received.show()

final_df = new_records.select(*columns).union(update_records.select(*columns)).union(not_received.select(*columns))
print("final")
final_df.show()


df_write(df=final_df, expected_table='[silver].[Customer_Current_expected]')




