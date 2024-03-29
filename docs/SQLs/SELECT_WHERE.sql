-- REFERS : https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_columns

-- SELECT *
-- FROM Customers
-- WHERE CustomerID >= 80;  -- COUNT : 12

-- SELECT *
-- FROM Customers
-- WHERE CustomerID <> 80;  -- COUNT :90

-- SELECT *
-- FROM Customers
-- WHERE CustomerID BETWEEN 20 AND 30; COUNT : 11

-- SELECT *
-- FROM Customers
-- WHERE CustomerID >= 20 AND CustomerID <= 30; -- COUNT : 11

-- SELECT *
-- FROM Customers
-- WHERE CustomerID IN (1,10,15,20) -- COUNT : 4

-- SELECT *
-- FROM Customers
-- WHERE City = 'London' -- COUNT : 6

-- SELECT *
-- FROM Customers
-- WHERE City IN ('London','Berlin')
-- AND CustomerID <= 11 --COUNT : 3
-- ;