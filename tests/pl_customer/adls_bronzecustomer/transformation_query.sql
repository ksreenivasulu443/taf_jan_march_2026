SELECT *
FROM bronze.Customer_bronze
WHERE SourceFileName IN (
    SELECT SourceFileName
    FROM (
        SELECT TOP (1)
            SourceFileName
        FROM bronze.Customer_bronze
        GROUP BY SourceFileName
        ORDER BY MAX(InsertDate) DESC
    ) AS LatestFile
)