SELECT
    StateName,
    COUNT(CustomerID) AS totalcustomers
FROM silver.Customer_Current
GROUP BY StateName