import pyodbc

# SQL Server Connection Details
server = "sqlserverretail756.database.windows.net"
database = "retaildb"
username = "retaildbadmin"
password = "Dharmavaram1@"

# Connection String
conn_str = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
)

merge_query = """
WITH Dedup AS
(
    SELECT
        CustomerID,
        CustomerName,
        Email,
        PhoneNumber,
        City,
        StateName,
        SourceFileName,
        InsertDate,
        HashKey,
        ROW_NUMBER() OVER
        (
            PARTITION BY CustomerID
            ORDER BY InsertDate DESC
        ) AS RN
    FROM silver.Customer_Clean
)

MERGE silver.Customer_Current AS T
USING
(
    SELECT *
    FROM Dedup
    WHERE RN = 1
) AS S
ON T.CustomerID = S.CustomerID

WHEN MATCHED THEN
    UPDATE SET
        T.CustomerName = S.CustomerName,
        T.Email = S.Email,
        T.PhoneNumber = S.PhoneNumber,
        T.City = S.City,
        T.StateName = S.StateName,
        T.SourceFileName = S.SourceFileName,
        T.HashKey = S.HashKey,
        T.UpdateDate = GETDATE()

WHEN NOT MATCHED THEN
    INSERT
    (
        CustomerID,
        CustomerName,
        Email,
        PhoneNumber,
        City,
        StateName,
        SourceFileName,
        HashKey,
        InsertDate,
        UpdateDate
    )
    VALUES
    (
        S.CustomerID,
        S.CustomerName,
        S.Email,
        S.PhoneNumber,
        S.City,
        S.StateName,
        S.SourceFileName,
        S.HashKey,
        GETDATE(),
        GETDATE()
    );
"""

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    cursor.execute(merge_query)
    conn.commit()

    print("Customer_Current loaded successfully.")

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    cursor.close()
    conn.close()