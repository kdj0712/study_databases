-- REFERS : https://www.w3schools.com/mysql/trymysql.asp?filename=trysql_is_null


+ 조건 : 비 진성고객 리스트 필요

SELECT CustomerName, CNT,ORDER_COUNT
FROM (SELECT Customers.CustomerName, ORDERS_GROUP.CNT,
        CASE 
            WHEN ORDERS_GROUP.CNT <= 1 THEN 'LITTLE'
            WHEN ORDERS_GROUP.CNT IS NULL THEN 'LITTLE'
            ELSE 'BIG'
         END AS ORDER_COUNT
    FROM Customers
        LEFT JOIN (SELECT CustomerID,COUNT(CustomerID) AS CNT
                FROM Orders
                GROUP BY CustomerID
                ) AS ORDERS_GROUP
        ON Customers.CustomerID = ORDERS_GROUP.CustomerID) AS FilteredResults
WHERE ORDER_COUNT = 'LITTLE'
ORDER BY CustomerName;
RESULT = 3

+ 조건 : 판매자 중 수익 낮은 순위자 3명 정보, 총 판매액
SELECT Employees.*, TotalSales.SUM_TOTAL
FROM Employees
LEFT JOIN (
    SELECT Orders.EmployeeID, SUM(OrderDetails.Quantity * Products.Price) AS SUM_TOTAL
    FROM Orders
    INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
    INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
    GROUP BY Orders.EmployeeID
) AS TotalSales ON Employees.EmployeeID = TotalSales.EmployeeID
ORDER BY TotalSales.SUM_TOTAL ASC
LIMIT 3
;
-- EmployeeID     LastName	    FirstName	 BirthDate	         Photo	        Notes	SUM_TOTAL
-- 5	Buchanan	Steven	1955-03-04	EmpID5.pic	Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree. Upon joining the company as a sales representative, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London, where he was promoted to sales manager. Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management'. He is fluent in French.	81745.85
-- 6	Suyama	Michael	1963-07-02	EmpID6.pic	Michael is a graduate of Sussex University (MA, economics) and the University of California at Los Angeles (MBA, marketing). He has also taken the courses 'Multi-Cultural Selling' and 'Time Management for the Sales Professional'. He is fluent in Japanese and can read and write French, Portuguese, and Spanish.	83673.45
-- 9	Dodsworth	Anne	1969-07-02	EmpID9.pic	Anne has a BA degree in English from St. Lawrence College. She is fluent in French and German.	86566.60
+ 조건 : 배송 회사별 총 배송 건수와 총 제품 금액 정보

SELECT Shippers.*, TotalSales.SUM_TOTAL, TotalDeliveries.DELIVERY
FROM Shippers
LEFT JOIN (
    SELECT Orders.ShipperID, SUM(OrderDetails.Quantity * Products.Price) AS SUM_TOTAL
    FROM Orders
    INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
    INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
    GROUP BY Orders.ShipperID
) AS TotalSales ON Shippers.ShipperID = TotalSales.ShipperID
LEFT JOIN (
    SELECT ShipperID, COUNT(ShipperID) AS DELIVERY
    FROM Orders
    GROUP BY ShipperID
) AS TotalDeliveries ON Shippers.ShipperID = TotalDeliveries.ShipperID
ORDER BY TotalSales.SUM_TOTAL ASC
;

-- ShipperID	ShipperName 	        Phone	        SUM_TOTAL	       DELIVERY
--      1	    Speedy Express	    (503) 555-9831	    395931.17       	249
--      3	    Federal Shipping	(503) 555-9931	    442546.25	        255
--      2	    United Package	    (503) 555-3199  	610889.89	        326
+ 조건 : 제품 회사별 총 판매액과 정보
SELECT Suppliers.*, SUM(OrderDetails.Quantity * Products.Price) AS SUM_TOTAL
FROM Suppliers
    INNER JOIN Products ON Suppliers.SupplierID = Products.SupplierID
    INNER JOIN OrderDetails ON Products.ProductID = OrderDetails.ProductID
GROUP BY Suppliers.SupplierID
ORDER BY Suppliers.SupplierID
;

-- SupplierID	SupplierName	ContactName	Address	City	PostalCode	Country	Phone	SUM_TOTAL
-- 1	Exotic Liquid	Charlotte Cooper	49 Gilbert St.	Londona	EC1 4SD	UK	(171) 555-2222	38267.00
-- 2	New Orleans Cajun Delights	Shelley Burke	P.O. Box 78934	New Orleans	70117	USA	(100) 555-4822	36073.55
-- 3	Grandma Kelly's Homestead	Regina Murphy	707 Oxford Rd.	Ann Arbor	48104	USA	(313) 555-5735	45295.00
-- 4	Tokyo Traders	Yoshi Nagase	9-8 Sekimai Musashino-shi	Tokyo	100	Japan	(03) 3555-5011	35187.00
-- 5	Cooperativa de Quesos 'Las Cabras'	Antonio del Valle Saavedra	Calle del Rosal 4	Oviedo	33007	Spain	(98) 598 76 54	27898.00
-- 6	Mayumi's	Mayumi Ohno	92 Setsuko Chuo-ku	Osaka	545	Japan	(06) 431-7877	16630.00
-- 7	Pavlova, Ltd.	Ian Devling	74 Rose St. Moonie Ponds	Melbourne	3058	Australia	(03) 444-2343	123827.10
-- 8	Specialty Biscuits, Ltd.	Peter Wilson	29 King's Way	Manchester	M14 GSD	UK	(161) 555-4448	52152.10
-- 9	PB Knäckebröd AB	Lars Peterson	Kaloadagatan 13	Göteborg	S-345 67	Sweden	031-987 65 43	12528.00
-- 10	Refrescos Americanas LTDA	Carlos Diaz	Av. das Americanas 12.890	São Paulo	5442	Brazil	(11) 555 4640	5062.50
-- 11	Heli Süßwaren GmbH & Co. KG	Petra Winkler	Tiergartenstraße 5	Berlin	10785	Germany	(010) 9984510	43991.69
-- 12	Plutzer Lebensmittelgroßmärkte AG	Martin Bein	Bogenallee 51	Frankfurt	60439	Germany	(069) 992755	165370.59
-- 13	Nord-Ost-Fisch Handelsgesellschaft mbH	Sven Petersen	Frahmredder 112a	Cuxhaven	27478	Germany	(04721) 8713	15844.68
-- 14	Formaggi Fortini s.r.l.	Elio Rossi	Viale Dante, 75	Ravenna	48100	Italy	(0544) 60323	55015.30
-- 15	Norske Meierier	Beate Vileid	Hatlevegen 5	Sandvika	1320	Norway	(0)2-953010	50317.00
-- 16	Bigfoot Breweries	Cheryl Saylor	3400 - 8th Avenue Suite 210	Bend	97101	USA	(503) 555-9931	25554.00
-- 17	Svensk Sjöföda AB	Michael Björn	Brovallavägen 231	Stockholm	S-123 45	Sweden	08-123 45 67	22940.00
-- 18	Aux joyeux ecclésiastiques	Guylène Nodier	203, Rue des Francs-Bourgeois	Paris	75004	France	(1) 03.83.00.68	178434.50
-- 19	New England Seafood Cannery	Robb Merchant	Order Processing Dept. 2100 Paul Revere Blvd.	Boston	02134	USA	(617) 555-3267	29761.85
-- 20	Leka Trading	Chandra Leka	471 Serangoon Loop, Suite #402	Singapore	0512	Singapore	555-8787	48127.45
-- 21	Lyngbysild	Niels Petersen	Lyngbysild Fiskebakken 10	Lyngby	2800	Denmark	43844108	11402.00
-- 22	Zaanse Snoepfabriek	Dirk Luchte	Verkoop Rijnweg 22	Zaandam	9999 ZZ	Netherlands	(12345) 1212	6367.00
-- 23	Karkki Oy	Anne Heikkonen	Valtakatu 12	Lappeenranta	53120	Finland	(953) 10956	31876.75
-- 24	G'day, Mate	Wendy Mackenzie	170 Prince Edward Parade Hunter's Hill	Sydney	2042	Australia	(02) 555-5914	74139.60
-- 25	Ma Maison	Jean-Guy Lauzon	2960 Rue St. Laurent	Montréal	H1J 1C3	Canada	(514) 555-9022	27296.75
-- 26	Pasta Buttini s.r.l.	Giovanni Giudici	Via dei Gelsomini, 153	Salerno	84100	Italy	(089) 6547665	56457.00
-- 27	Escargots Nouveaux	Marie Delamare	22, rue H. Voiron	Montceau	71300	France	85.57.00.07	7075.50
-- 28	Gai pâturage	Eliane Noz	Bat. B 3, rue des Alpes	Annecy	74000	France	38.76.98.06	135898.00
-- 29	Forêts d'érables	Chantal Goulet	148 rue Chasseur	Ste-Hyacinthe	J2S 7S8	Canada	(514) 555-2955	70577.40

+ 조건 : 카테고리별 판매 합계 정보
SELECT Categories.*, SUM(OrderDetails.Quantity * Products.Price) AS SUM_TOTAL
FROM Categories
    INNER JOIN Products ON Categories.CategoryID = Products.CategoryID
    INNER JOIN OrderDetails ON Products.ProductID = OrderDetails.ProductID
GROUP BY Categories.CategoryID 
ORDER BY Categories.CategoryID
;

-- CategoryID	  CategoryName	    Description	                                                SUM_TOTAL
--     1           Beverages	    Soft drinks, coffees, teas, beers, and ales	                309582.25
--     2           Condiments	    Sweet and savory sauces, relishes, spreads, and seasonings	122343.00
--     3	       Confections	    Desserts, candies, and sweet breads	                        190328.54
--     4	       Dairy Products	Cheeses                                                 	269128.30
--     5	       Grains/Cereals	Breads, crackers, pasta, and cereal	                        106848.00
--     6	       Meat/Poultry     Prepared meats                                          	190682.69
--     7           Produce      	Dried fruit and bean curd                               	111395.00
--     8	       Seafood	        Seaweed and fish	                                        149059.53