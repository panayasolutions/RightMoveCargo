CREATE TABLE `mtBranch` (
  `branch_code` INT NOT NULL,
  `branch_name` VARCHAR(100) NULL,
  PRIMARY KEY (`branch_code`)
);

CREATE TABLE `mtCourierType` (
  `courier_type_code` INT NOT NULL,
  `courier_name` VARCHAR(100) NULL,
  PRIMARY KEY (`courier_type_code`)
);
CREATE TABLE `mpBranchCourierType` (
  `branch_courier_type_code` INT NOT NULL,
  `branch_code` INT NOT NULL,
  `courier_type_code` INT NOT NULL,
  PRIMARY KEY (`branch_courier_type_code`),
  CONSTRAINT `branch_code` FOREIGN KEY (`branch_code`) REFERENCES `mtBranch` (`branch_code`),
  CONSTRAINT `courier_type_code` FOREIGN KEY (`courier_type_code`) REFERENCES `mtCourierType` (`courier_type_code`),
);

CREATE TABLE `mtCourierMode` (
  `courier_mode_code` INT NOT NULL,
  `courier_name` VARCHAR(100) NULL,
  PRIMARY KEY (`courier_mode_code`)
);

CREATE TABLE `mpCourierModeType` (
  `courier_mode_type_code` INT NOT NULL,
  `courier_type_code` INT NOT NULL,
  `courier_mode_code` INT NOT NULL,
  PRIMARY KEY (`courier_mode_type_code`),
  CONSTRAINT `courier_type_code` FOREIGN KEY (`courier_type_code`) REFERENCES `mtCourierType` (`courier_type_code`),
  CONSTRAINT `courier_mode_code` FOREIGN KEY (`courier_mode_code`) REFERENCES `mtCourierMode` (`courier_mode_code`),
);

CREATE TABLE `mpBranchCourierMode` (
  `branch_courier_mode_code` INT NOT NULL,
  `branch_code` INT NOT NULL,
  `courier_type_code` INT NOT NULL,
  `courier_mode_code` INT NOT NULL,
  PRIMARY KEY (`branch_courier_mode_code`),
  CONSTRAINT `branch_code` FOREIGN KEY (`branch_code`) REFERENCES `mtBranch` (`branch_code`),
  CONSTRAINT `courier_type_code` FOREIGN KEY (`courier_type_code`) REFERENCES `mtCourierType` (`courier_type_code`),
  CONSTRAINT `courier_mode_code` FOREIGN KEY (`courier_mode_code`) REFERENCES `mtCourierMode` (`courier_mode_code`),
);

CREATE TABLE `mtUserType` (
  `user_type_code` INT NOT NULL,
  `user_type_name` VARCHAR(100) UNIQUE NOT NULL,
  PRIMARY KEY (`user_type_code`)
);

CREATE TABLE `mtUser` (
  `user_code` INT UNIQUE NOT NULL,
  `user_name` VARCHAR(100) UNIQUE NOT NULL,
  `user_type_code` VARCHAR(100) NOT NULL,
   FOREIGN KEY (`user_type_code`) REFERENCES `mtUserType` (`user_type_code`),
  PRIMARY KEY (`user_code`)
);

CREATE TABLE `mpUserBranch` (
  `user_branch_code` INT NOT NULL,
  `user_code` INT NOT NULL,
  `user_type_code` INT NOT NULL,
  `branch_code` INT NOT NULL,
   `branch_courier_type_code` INT NOT NULL,
   FOREIGN KEY (`user_code`) REFERENCES `mtUser` (`user_code`),
   FOREIGN KEY (`branch_code`) REFERENCES `mtBranch` (`branch_code`),
   FOREIGN KEY (`user_type_code`) REFERENCES `mtUserType` (`user_type_code`),
   FOREIGN KEY (`branch_courier_type_code`) REFERENCES `mpBranchCourierType` (`branch_courier_type_code`),
   PRIMARY KEY (`user_branch_code`)
);

INSERT INTO `mtUserBranch` (`user_branch_code`, `user_code`, `user_type_code`, `branch_code`) VALUES
 ('1001', '501', '2', '1'),
 ('1002', '502', '2', '3'),
 ('1003', '503', '2', '2'),
 ('1004', '504', '1', '1'),
 ('1005', '504', '1', '3'),
 ('1006', '505', '1', '3'),
 ('1007', '506', '1', '2')


CREATE TABLE `mtBranch` (
  `branch_code` INT NOT NULL,
  `branch_name` VARCHAR(100) NULL,
  PRIMARY KEY (`branch_code`)
);

INSERT INTO `mtUserBranch` (`user_branch_code`, `user_code`, `user_type_code`, `branch_code`) VALUES 
('1001', '501', '2', '1'),
('1002', '502', '2', '3'), 
('1003', '503', '2', '2'),
('1004', '504', '1', '1'),
('1005', '504', '1', '3'),
('1006', '505', '1', '3'),
('1007', '506', '1', '2')

INSERT INTO `mtUser` (`user_code`, `user_name`, `user_type_code`) VALUES 
('501', 'Employee', '2')
('502', 'Employee', '2')
('503', 'Employee', '2')
('504', 'Client1', '1')
('505', 'Client2', '1')
('506', 'Client3', '1')
('507', 'Admin', '3');



INSERT INTO `mpBranchCourierMode` (`branch_courier_mode_code`, `branch_code`, `courier_type_code`, `courier_mode_code`, `user_id`) 
VALUES ('1000', '1', '1000', '200', '508'), 
('1001', '1', '2000', '200', '508'), 
('1002', '1', '3000', '200', '508'), 
('1003', '1', '4000', '200', '508'), 
('1004', '1', '1000', '100', '508'), 
('1005', '1', '2000', '100', '508'), 
('1006', '2', '1000', '200', '508'), 
('1007', '2', '2000', '200', '508'),
('1008', '2', '4000', '100', '508')

SELECT * FROM `mtUser` as amtUser
JOIN mpUserBranch as ampUserBranch on ampUserBranch.user_code = amtUser.user_code
JOIN mtUserType as amtUserType on amtUserType.user_type_code = ampUserBranch.user_type_code
LEFT JOIN mtBranch as amtBranch on amtBranch.branch_code = ampUserBranch.branch_code
WHERE amtUser.user_name='Client1';


// Support by Branch 
SELECT * FROM mtBranch as brc
INNER JOIN mpBranchCourierMode as bcm on bcm.branch_code=brc.branch_code
LEFT JOIN mtCourierMode as amod on amod.courier_mode_code = bcm.courier_mode_code
LEFT JOIN mtCourierType as atype on atype.courier_type_code = bcm.courier_type_code
WHERE brc.branch_code='3'


// RMC Employee
SELECT * FROM `mtUser` as amtUser
JOIN mpUserBranch as ampUserBranch on ampUserBranch.user_code = amtUser.user_code
JOIN mtUserType as amtUserType on amtUserType.user_type_code = ampUserBranch.user_type_code
LEFT JOIN mtBranch as amtBranch on amtBranch.branch_code = ampUserBranch.branch_code
WHERE amtUser.user_name='Employee1';


// Employee or Client by user type and Branch 
SELECT * FROM `mtUser` as amtUser
JOIN mpUserBranch as ampUserBranch on ampUserBranch.user_code = amtUser.user_code
JOIN mtUserType as amtUserType on amtUserType.user_type_code = ampUserBranch.user_type_code
LEFT JOIN mtBranch as amtBranch on amtBranch.branch_code = ampUserBranch.branch_code
WHERE amtBranch.branch_code='1' and amtUser.user_type_code = 1;




TABLE  MENU,ID,TABNAME,TABTYPE,PTABID,PTABID
TABNAME(ORDER,INSCAN,PINCODE FINDER,CLIEN NAME,PINCODE)
TABTYPE(TAB,INSIDE FIELD)
PTABID ORDER 

USER_TYPE
BRANCH


mpMenuBranch
MenuId,user_branch_code, visible,edit,delete,













CREATE TABLE mtConsignee(
ConsCode varchar(10) NOT NULL,
ConsName varchar(100) NOT NULL,
Address1 varchar(100) NOT NULL,
Address2 varchar(100) NOT NULL,
Address3 varchar(100) NOT NULL,
Pin varchar(6) NOT NULL,
Phone varchar(100) NOT NULL,
Mobile varchar(100) NOT NULL,
EmailId varchar(100) NOT NULL,
Active varchar(3) NOT NULL,
ActiveDate datetime NOT NULL,
CustomerCode varchar(10) NOT NULL,
EnterBy varchar(10) NOT NULL,
EnterDateTime datetime NOT NULL,
EditBy varchar(10) NOT NULL,
EditDateTime datetime NOT NULL,
StateName varchar (100) ,
BranchInCharge varchar (100),
)
 CONSTRAINT PK_mtCons  PRIMARY KEY CLUSTERED
(
[ConsCode] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]





     'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': "RevenueTest",
        'USER':'xa',
        'PASSWORD':'Xp_256$',
        'HOST':'103.65.20.180',
        'PORT':'33893',
        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
        },
		

import pyodbc
db = pyodbc.connect('driver={%s};server=%s;database=%s;uid=%s;pwd=%s' % ( 'ODBC Driver 17 for SQL Server', '103.65.20.180,33893', 'RevenueTest', 'xa', 'Xp_256$' ) )
cursor = db.cursor()
cursor.execute('SELECT * FROM dummy')
for row in cursor:
    print(row)