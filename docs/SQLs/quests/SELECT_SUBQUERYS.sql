- 다음 조건은 subquery 사용
- Table : Customers, Orders
+ 조건 : 주문 갯수가 5개 이상인 CustomerName 찾기
SELECT CustomerName
FROM Customers
WHERE CustomerID IN (SELECT CustomerID
                     FROM Orders
                     GROUP BY CustomerID
                     HAVING COUNT(CustomerID) >= 5)
;
RESULT = [
            ,'Alfreds Futterkiste'
            ,'Antonio Moreno Taquería'
            ,'Around the Horn'
            ,'Berglunds snabbköp'
            ,'Blauer See Delikatessen'
            ,'Blondel père et fils'
            ,'Bon app'
            ,'Bottom-Dollar Marketse'
            ,"B's Beverages"
            ,'Cactus Comidas para llevar'
            ,'Chop-suey Chinese'
            ,'Comércio Mineiro'
            ,'Drachenblut Delikatessend'
            ,'Eastern Connection'
            ,'Ernst Handel'
            ,'Familia Arquibaldo'
            ,'Folies gourmandes'
            ,'Folk och fä HB'
            ,'Frankenversand'
            ,'Franchi S.p.A.'
            ,'Furia Bacalhau e Frutos do Mar'
            ,'Galería del gastrónomo'
            ,'Godos Cocina Típica'
            ,'Gourmet Lanchonetes'
            ,'Great Lakes Food Market'
            ,'Hanari Carnes'
            ,'HILARIÓN-Abastos'
            ,'Hungry Coyote Import Store'
            ,'Hungry Owl All-Night Grocers'
            ,'Island Trading'
            ,'Königlich Essen'
            ,"La maison d'Asie"
            ,'Lehmanns Marktstand'
            ,'LILA-Supermercado'
            ,'LINO-Delicateses'
            ,'Lonesome Pine Restaurant'
            ,'Magazzini Alimentari Riuniti'
            ,'Maison Dewey'
            ,'Mère Paillarde'
            ,'Morgenstern Gesundkost'
            ,'Océano Atlántico Ltda.'
            ,'Old World Delicatessen'
            ,'Ottilies Käseladen'
            ,'Pericles Comidas clásicas'
            ,'Piccolo und mehr'
            ,'Princesa Isabel Vinhoss'
            ,'Que Delícia'
            ,'Queen Cozinha'
            ,'QUICK-Stop'
            ,'Rancho grande'
            ,'Rattlesnake Canyon Grocery'
            ,'Reggiani Caseifici'
            ,'Ricardo Adocicados'
            ,'Richter Supermarkt'
            ,'Romero y tomillo'
            ,'Santé Gourmet'
            ,'Save-a-lot Markets'
            ,'Seven Seas Imports'
            ,'Simons bistro'
            ,'Split Rail Beer & Ale'
            ,'Suprêmes délices'
            ,'Toms Spezialitäten'
            ,'Tortuga Restaurante'
            ,'Tradição Hipermercados'
            ,'Vaffeljernet'
            ,'Victuailles en stock'
            ,'Die Wandernde Kuh'
            ,'Wartian Herkku'
            ,'Wellington Importadora'
            ,'White Clover Markets'
            ,'Wilman Kala'
            ,'Wolski']
            
- Table : Orders
+ 조건 : 주문 갯수가 20개 이상인 배송자
SELECT LastName,FirstName
FROM Employees
WHERE EmployeeID IN (SELECT EmployeeID
                    FROM Orders
                    GROUP BY EmployeeID
                    HAVING COUNT(EmployeeID) >= 20)
;
RESULT = ['Davolio, Nancy'
        ,'Fuller, Andrew'
        ,'Leverling, Janet'
        ,'Peacock, Margaret'
        ,'Buchanan, Steven'
        ,'Suyama, Michael'
        ,'King, Robert'
        ,'Callahan, Laura'
        ,'Dodsworth, Anne']


- Table : Suppliers
+ 조건 : CategoryID를 가장 많이 제공 상위 2개 회사 정보


SELECT Category_GROUP.SupplierID, COUNT(Category_GROUP.SupplierID) AS CSD
FROM (SELECT SupplierID, CategoryID, COUNT(CategoryID) AS CNT
        FROM Products
        WHERE 1 = 1
        GROUP BY SupplierID, CategoryID
    )AS Category_GROUP
WHERE 1 = 1
GROUP BY Category_GROUP.SupplierID


SELECT Category_GROUP.SupplierID, COUNT(Category_GROUP.SupplierID) AS CSD
FROM (SELECT SupplierID, CategoryID, COUNT(CategoryID) AS CNT
        FROM Products
        WHERE 1 = 1
        GROUP BY SupplierID, CategoryID
    )AS Category_GROUP
WHERE 1 = 1
GROUP BY Category_GROUP.SupplierID
ORDER BY COUNT(Category_GROUP.SupplierID) DESC
LIMIT 0, 2

SELECT *
FROM Suppliers
WHERE SupplierID = (SELECT Category_GROUP.SupplierID, COUNT(Category_GROUP.SupplierID) AS CSD
                    FROM (SELECT SupplierID, CategoryID, COUNT(CategoryID) AS CNT
                            FROM Products
                            WHERE 1 = 1
                            GROUP BY SupplierID, CategoryID
                        )AS Category_GROUP
                    WHERE 1 = 1
                    GROUP BY Category_GROUP.SupplierID
                    ORDER BY COUNT(Category_GROUP.SupplierID) DESC
                    LIMIT 0, 2
)
