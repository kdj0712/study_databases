-- COMPANY codes
INSERT INTO `COMMON_CODES` (`FK_COMMON_CODES`, `PART_NAME`, `NAME`) VALUES 
('CP_01', 'COMPANY', '현대'),
('CP_02', 'COMPANY', '기아'),
('CP_03', 'COMPANY', '쉐보레'),
('CP_04', 'COMPANY', 'BMW'),
('CP_05', 'COMPANY', '벤츠');

-- CAR codes
INSERT INTO `COMMON_CODES` (`FK_COMMON_CODES`, `PART_NAME`, `NAME`) VALUES 
('CAR_01', 'CAR', '소나타'),
('CAR_02', 'CAR', '쏘렌토'),
('CAR_03', 'CAR', '카마로'),
('CAR_04', 'CAR', '3시리즈'),
('CAR_05', 'CAR', 'E클래스');

-- YEAR codes
INSERT INTO `COMMON_CODES` (`FK_COMMON_CODES`, `PART_NAME`, `NAME`) VALUES 
('YEAR_01', 'YEAR', '2020'),
('YEAR_02', 'YEAR', '2018'),
('YEAR_03', 'YEAR', '2019'),
('YEAR_04', 'YEAR', '2017'),
('YEAR_05', 'YEAR', '2021'),
('YEAR_06', 'YEAR', '2018');


INSERT INTO `CAR_INFO` (`PK_CAR_ID`, `CAR_NAME`, `FK_COMMON_CODES_COMPANY`, `FK_COMMON_CODES_YEARS`) VALUES 
('CAR_01', '소나타', 'CP_01', 'YEAR_01'),
('CAR_02', '쏘렌토', 'CP_02', 'YEAR_02'),
('CAR_03', '카마로', 'CP_03', 'YEAR_03'),
('CAR_04', '3시리즈', 'CP_04', 'YEAR_04'),
('CAR_05', 'E클래스', 'CP_05', 'YEAR_05'),
('CAR_06', '소나타', 'CP_01', 'YEAR_02');