SELECT COUNT(Country) AS CNT, Country, MAX(PostalCode) AS MAX_POST
FROM Customers
GROUP BY Country;
