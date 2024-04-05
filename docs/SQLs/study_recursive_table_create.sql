CREATE TABLE `DEPARTMENTS` (
    `CHILD_ID` INT NOT NULL,
    `DEPARTMENT_NAME` VARCHAR(100) NOT NULL,
    `PARENT_ID` INT,
    PRIMARY KEY (`CHILD_ID`),
    FOREIGN KEY (`PARENT_ID`) REFERENCES `DEPARTMENTS`(`CHILD_ID`)
);
INSERT INTO `DEPARTMENTS` (`CHILD_ID`, `DEPARTMENT_NAME`, `PARENT_ID`) VALUES
(1, '회사', NULL),
(2, '기술부', 1),
(3, '인사부', 1),
(4, '개발팀', 2),
(5, '디자인팀', 2);

INSERT INTO `DEPARTMENTS` (`CHILD_ID`, `DEPARTMENT_NAME`, `PARENT_ID`) VALUES
(16, 'WEB 개발', 4),
(6, '인사팀', 3),
(7, '채용팀', 3),
(8, '재무부', 1),
(9, '회계팀', 8),
(10, '감사팀', 8),
(11, '마케팅부', 1),
(12, '내부마케팅팀', 11),
(13, '외부마케팅팀', 11),
(14, '고객지원부', 1),
(15, '콜센터팀', 14);

SELECT *
FROM DEPARTMENTS
;

WITH RECURSIVE SubDepartments AS (
    SELECT  -- SELECT의 갯수가 가장 중요
        D.CHILD_ID,
        D.DEPARTMENT_NAME,
        D.PARENT_ID
    FROM
        DEPARTMENTS D
    WHERE
        D.PARENT_ID = 1 -- 기술부의 CHILD_ID
    UNION ALL
    SELECT
        D.CHILD_ID,
        D.DEPARTMENT_NAME,
        D.PARENT_ID
    FROM
        DEPARTMENTS D
    INNER JOIN
        SubDepartments SD ON D.PARENT_ID = SD.CHILD_ID
)
SELECT * FROM SubDepartments;


WITH RECURSIVE SubDepartments AS (
    SELECT  -- SELECT의 갯수가 가장 중요
        D.CHILD_ID,
        D.DEPARTMENT_NAME,
        D.PARENT_ID
    FROM
        DEPARTMENTS D
    WHERE
        D.CHILD_ID = 15 -- 기술부의 CHILD_ID
    UNION ALL
    SELECT
        D.CHILD_ID,
        D.DEPARTMENT_NAME,
        D.PARENT_ID
    FROM
        DEPARTMENTS D
    INNER JOIN
        SubDepartments SD ON D.CHILD_ID = SD.PARENT_ID
)
SELECT * FROM SubDepartments;
