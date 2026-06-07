SELECT
    CustomerID,
    UPPER(TRIM(CustomerName)) AS CustomerName,
    LOWER(TRIM(Email)) AS Email,
    LTRIM(RTRIM(PhoneNumber)) AS PhoneNumber,
    ISNULL(UPPER(City), 'UNKNOWN') AS City,
    ISNULL(UPPER(StateName), 'UNKNOWN') AS StateName,
    SourceFileName,
    InsertDate,
    HashKey
FROM bronze.Customer_bronze