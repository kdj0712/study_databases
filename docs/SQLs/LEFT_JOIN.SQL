-- ORDERS 테이블에서 고객의 구매 이력 확인하기
SELECT CustomerID,COUNT(CustomerID) AS CNT
FROM Orders
GROUP BY CustomerID
;

-- 고객의 정보를 ORDERS 테이블과 결합하기 WITH LEFT JOIN
SELECT Customers.CustomerName,ORDERS_GROUP.CustomerID, ORDERS_GROUP.CNT
FROM Customers
	LEFT JOIN (SELECT CustomerID,COUNT(CustomerID) AS CNT
                                  FROM Orders
                                  GROUP BY CustomerID
                                  ) AS ORDERS_GROUP
	ON Customers.CustomerID=ORDERS_GROUP.CustomerID
ORDER BY Customers.CustomerName
;

-- 미구매고객의 정보를 가져오기 WITH LEFT JOIN AND IS NULL
SELECT Customers.CustomerName,ORDERS_GROUP.CustomerID
FROM Customers
	LEFT JOIN (SELECT CustomerID,COUNT(CustomerID) AS CNT
                                  FROM Orders
                                  GROUP BY CustomerID
                                  ) AS ORDERS_GROUP
	ON Customers.CustomerID=ORDERS_GROUP.CustomerID
    WHERE ORDERS_GROUP.CustomerID IS NULL
ORDER BY Customers.CustomerName;

-- 반대의 경우는 IS NOT NULL을 이용
SELECT Customers.CustomerName,ORDERS_GROUP.CustomerID, ORDERS_GROUP.CNT
FROM Customers
	LEFT JOIN (SELECT CustomerID,COUNT(CustomerID) AS CNT
                                  FROM Orders
                                  GROUP BY CustomerID
                                  ) AS ORDERS_GROUP
	ON Customers.CustomerID=ORDERS_GROUP.CustomerID
    WHERE ORDERS_GROUP.CustomerID IS NOT NULL
ORDER BY Customers.CustomerName;
