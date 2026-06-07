SELECT
        StateName,
        COUNT(CustomerID)
    FROM silver.Customer_Current
    GROUP BY StateName