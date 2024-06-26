CREATE TABLE `COMMON_CODES` (
	`FK_COMMON_CODES`	VARCHAR(50)	NOT NULL,
	`PART_NAME`	VARCHAR(255)	NULL,
	`NAME`	VARCHAR(255)	NULL
);
CREATE TABLE `USERS` (
	`PK_USERS`	VARCHAR(50)	NOT NULL,
	`NAME`	VARCHAR(255)	NULL,
	`PHONE`	VARCHAR(255)	NULL,
	`EMAIL`	VARCHAR(255)	NULL,
	`FK_COMMON_CODES`	VARCHAR(255)	NULL
);
CREATE TABLE `DELIVERY_PLACES` (
	`PK_DELIVERY_PLACES`	VARCHAR(50)	NOT NULL,
	`PK_USERS`	VARCHAR(50)	NOT NULL,
	`FK_COMMON_CODES`	VARCHAR(50)	NULL
);
ALTER TABLE `COMMON_CODES` ADD CONSTRAINT `PK_COMMON_CODES` PRIMARY KEY (
	`FK_COMMON_CODES`
);
ALTER TABLE `USERS` ADD CONSTRAINT `PK_USERS` PRIMARY KEY (
	`PK_USERS`
);
ALTER TABLE `DELIVERY_PLACES` ADD CONSTRAINT `PK_DELIVERY_PLACES` PRIMARY KEY (
	`PK_DELIVERY_PLACES`,
	`PK_USERS`
);
ALTER TABLE `DELIVERY_PLACES` ADD CONSTRAINT `FK_USERS_TO_DELIVERY_PLACES_1` FOREIGN KEY (
	`PK_USERS`
)
REFERENCES `USERS` (
	`PK_USERS`
);