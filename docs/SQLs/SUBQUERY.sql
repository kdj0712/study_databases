-- REFERS : https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_columns

-- 조건2 : 주문 갯수가 5개 이상인 CustomerName 찾기
-- table : Orders
SELECT COUNT(CustomerID) AS CNT, CustomerID
FROM Orders
GROUP BY CustomerID
HAVING COUNT(CustomerID) >= 5
ORDER BY CustomerID ASC;
-- Number of Records: 9 / CustomerID : 20, 37, 41, 46, 51, 63, 65, 75, 87
-- table : Customers
SELECT CustomerID, CustomerName
FROM Customers
WHERE CustomerID IN (20, 37, 41, 46, 51, 63, 65, 75, 87);
-- Number of Records: 9 / CustomerName : Ernst Handel, Hungry Owl All-Night Grocers, La maison d'Asie, LILA-Supermercado, Mère Paillarde, QUICK-Stop, Rattlesnake Canyon Grocery, Split Rail Beer & Ale, Wartian Herkku


--- 위 두 구문을 거의 결합한다면
SELECT *
FROM (SELECT COUNT(CustomerID) AS CNT, CustomerID
      FROM Orders
      GROUP BY CustomerID
      HAVING COUNT(CustomerID) >= 5
      ORDER BY CustomerID ASC
)
;

--- ALIAS 적용 구문

SELECT SUB_ORDERS.CNT, SUB_ORDERS.CustomerID
FROM (SELECT COUNT(CustomerID) AS CNT, CustomerID
      FROM Orders
      GROUP BY CustomerID
      HAVING COUNT(CustomerID) >= 5
      ORDER BY CustomerID ASC
) AS SUB_ORDERS
;


-- IS NULL
SELECT COUNT(*),CustomerName, ContactName, Address
FROM Customers
WHERE Address IS NULL;


-- NOT NULL
SELECT COUNT(*),CustomerName, ContactName, Address
FROM Customers
WHERE Address IS NOT NULL;

-- LIMIT 
SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address IS NOT NULL 
LIMIT 5,2
;

-- LIMIT WITH ORDER BY AND DESCENDING
SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address IS NOT NULL 
ORDER BY CustomerName DESC
LIMIT 5,2
;
