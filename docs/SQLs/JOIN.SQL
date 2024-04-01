SELECT * 
FROM Suppliers, Products
;

--  INNER JOIN
SELECT * 
FROM Products INNER JOIN Suppliers
	ON Suppliers.SupplierID = Products.SupplierID
;


-- INNER JOIN 이후 AND 조건 추가
SELECT * 
FROM Products INNER JOIN Suppliers
	ON Suppliers.SupplierID = Products.SupplierID
    AND SupplierName IN('Exotic Liquid','Tokyo Traders')
;

-- INNER JOIN 이후  ALIAS 적용
SELECT PRODUCT.SupplierID, SUPPLIER.SupplierID
FROM Products AS PRODUCT INNER JOIN Suppliers AS SUPPLIER
	ON SUPPLIER.SupplierID = PRODUCT.SupplierID
    AND SupplierName IN('Exotic Liquid','Tokyo Traders')
;

-- JOIN 적용 이후 다시 JOIN하기(내부의 ALIAS는 적용할 수 없음)
SELECT Categories.CategoryName, PRODUCT.SupplierID, SUPPLIER.SupplierID
FROM Products AS PRODUCT
INNER JOIN Suppliers AS SUPPLIER
	ON SUPPLIER.SupplierID = PRODUCT.SupplierID
    AND SUPPLIER.SupplierName IN('Exotic Liquid','Tokyo Traders')
INNER JOIN Categories
    ON PRODUCT.CategoryID = Categories.CategoryID;

SELECT Categories.*
FROM Products AS PRODUCT INNER JOIN Suppliers AS SUPPLIER
	ON SUPPLIER.SupplierID = PRODUCT.SupplierID
    AND SupplierName IN ('Exotic Liquid', 'Tokyo Traders')
     INNER JOIN Categories
        ON PRODUCT.CategoryID = Categories.CategoryID
;
-- LEFT JOIN
