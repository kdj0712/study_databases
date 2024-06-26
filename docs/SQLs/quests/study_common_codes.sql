SELECT *
FROM COMMON_CODES;

SELECT *
FROM CAR_INFO;

SELECT CAR_INFO.PK_CAR_ID,CAR_INFO.CAR_NAME , CC_YEAR.NAME AS `YEAR`, CC_COMPANY.NAME AS COMPANY
FROM CAR_INFO 
	JOIN COMMON_CODES AS CC_COMPANY
    ON CAR_INFO.FK_COMMON_CODES_COMPANY = CC_COMPANY.FK_COMMON_CODES
    JOIN COMMON_CODES AS CC_YEAR
    ON CAR_INFO.FK_COMMON_CODES_YEARS = CC_YEAR.FK_COMMON_CODES
;