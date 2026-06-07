SELECT *
FROM
(
    SELECT
        a.*,
        ROW_NUMBER() OVER
        (
            PARTITION BY InsertDate
            ORDER BY InsertDate DESC
        ) AS rn
    FROM bronze.Customer_bronze a
) x
WHERE rn = 1