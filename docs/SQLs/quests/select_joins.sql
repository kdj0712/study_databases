- Table : Customers, Orders
+ 조건 : CustomerName별로 주문 갯수 표시
SELECT CustomerName, COUNT(CustomerName)
FROM Customers INNER JOIN Orders
        ON Customers.CustomerID = Orders.CustomerID
    GROUP BY Orders.CustomerID
; 
RESULT = Number of Records: 89

- Table : OrderDetails 
+ 조건 : 제품명,가격, 주문 갯수, 고객명 표시
SELECT ProductName, Price, Quantity, CustomerName
FROM Products 
    INNER JOIN OrderDetails 
        ON Products.ProductID = OrderDetails.ProductID
    INNER JOIN Orders 
        ON Orders.OrderID = OrderDetails.OrderID
    INNER JOIN Customers 
        ON Customers.CustomerID = Orders.CustomerID;
RESULT = Number of Records: 2155

- Table : Orders
+ 조건 : 가장 많이 주문 받은 회사 직원명과 갯수
SELECT COUNT(*), Employees.LastName,Employees.FirstName	
FROM Orders
	INNER JOIN Employees
	    ON Orders.EmployeeID = Employees.EmployeeID
WHERE Orders.EmployeeID = (SELECT MAX(EmployeeID) FROM Orders)
GROUP BY Orders.EmployeeID, Employees.LastName,Employees.FirstName
;
RESULT 

COUNT(*)	LastName	FirstName
43      	Dodsworth	Anne