DROP DATABASE IF EXISTS AGRICULTURE;
CREATE DATABASE AGRICULTURE;
USE  AGRICULTURE;

DROP TABLE IF EXISTS Farmer;
CREATE TABLE Farmer (
  F_Aadhar_no BIGINT NOT NULL,
  Bankpassbook_no BIGINT NOT NULL,
  village_id BIGINT NOT NULL,
  scheme_id BIGINT NOT NULL,
  PRIMARY KEY (F_Aadhar_no,Bankpassbook_no,village_id,scheme_id)
);


INSERT INTO Farmer VALUES(783425631893,43528760231,43256,784);
INSERT INTO Farmer VALUES(923704280464,11463890352,30984,381);
INSERT INTO Farmer VALUES(410925727215,43528760231,03525,840);
INSERT INTO Farmer VALUES(392087826186,42697764432,89862,452);
INSERT INTO Farmer VALUES(194464669282,71743810711,73378,763);

DROP TABLE IF EXISTS Buyer;
CREATE TABLE Buyer (
   B_Aadhar_no BIGINT NOT NULL,
 market_id BIGINT NOT NULL,
  village_id BIGINT NOT NULL,
  PRIMARY KEY (B_Aadhar_no,village_id,market_id)
);

INSERT INTO Buyer VALUES(904157695876,659796,81645);
INSERT INTO Buyer VALUES(357624329684,999523,88924);
INSERT INTO Buyer VALUES(662765697619,389501,61388);
INSERT INTO Buyer VALUES(269777604798,080763,11953);


DROP TABLE IF EXISTS Personal_details;
CREATE TABLE Personal_details (
  Aadharcard_no BIGINT NOT NULL,
  fname varchar(50) NOT NULL,
  lname varchar(50) NOT NULL,
  Sex char(10) DEFAULT NULL,
  landsize float(15) NOT NULL,
  DOB VARCHAR(50),
   PRIMARY KEY (Aadharcard_no)
);

INSERT INTO Personal_details VALUES(783425631893,'ravi','reddy','m',6.2,'12/2/1982');
INSERT INTO Personal_details VALUES(923704280464,'venkata','naidu','m',7.94,'4/3/1962');
INSERT INTO Personal_details VALUES(410925727215,'neelima','chouary','f',9.23,'28/2/1975');
INSERT INTO Personal_details VALUES(392087826186,'sruthi','reddy','f',5.83,'3/7/1987');
INSERT INTO Personal_details VALUES(194464669282,'eswar','reddy','m',8.76,'1/10/1964');


DROP TABLE IF EXISTS Land;
CREATE TABLE Land (
  Land_reg_num BIGINT NOT NULL,
  owner_adhar_num BIGINT NOT NULL,
  geographical_location varchar(50),
   landsize float NOT NULL,
  soil_type varchar(50) NOT NULL,
   crops_grown_id int(50),
     PRIMARY KEY (Land_reg_num)
);

INSERT INTO Land VALUES(4875848794,783425631893,'24 la,38 lo',6.78,'red soil',643);
INSERT INTO Land VALUES(4879874985,923704280464,'67 la,46 lo',9.82,'black soil',973);
INSERT INTO Land VALUES(9068098594,410925727215,'56 la,72 lo',5.72,'red soil',572);
INSERT INTO Land VALUES(4567890678,392087826186,'62 la,92 lo',7.35,'black soil',562);
INSERT INTO Land VALUES(4567810983,194464669282,'73 la, 56 lo',5.92,'red soil',569);


DROP TABLE IF EXISTS Address;
CREATE TABLE Address (
  village_id INT NOT NULL,
  village_name varchar(50),
  pincode int(50),
  state varchar(50),
  country varchar(50),
   PRIMARY KEY (village_id)
);

INSERT INTO Address VALUES(59632,'kavali',567472,'Andra pradesh','india');
INSERT INTO Address VALUES(87589,'singavaram',587244,'Andra pradesh','india');
INSERT INTO Address VALUES(48984,'chukkulur',584387,'Andra pradesh','india');
INSERT INTO Address VALUES(34689,'bhimavaram',572103,'Andra pradesh','india');
INSERT INTO Address VALUES(84765,'kodumur',528790,'Andra pradesh','india');


DROP TABLE IF EXISTS village;
CREATE TABLE village (
  village_id BIGINT NOT NULL,
  no_of_farmers int,
  agricultural_land float,
    PRIMARY KEY (village_id)
);

INSERT INTO village VALUES(84679,346,1555.92);
INSERT INTO village VALUES(74957,205,1673.23);
INSERT INTO village VALUES(78674,493,1988.39);
INSERT INTO village VALUES(59698,689,6392.48);
INSERT INTO village VALUES(79965,453,9856.45);


DROP TABLE IF EXISTS Scheme;
CREATE TABLE Scheme(
  scheme_id INT NOT NULL,
  elgiblefarmers varchar(100) NOT NULL,
  benefits varchar(50),
  specification varchar(50),
  type varchar(50),
   PRIMARY KEY (scheme_id)
);


INSERT INTO Scheme VALUES(497,2384,'20,000','Farmers','state');
INSERT INTO Scheme VALUES(845,8749,'42,000','famers','central');
INSERT INTO Scheme VALUES(834,3769,'36,970','farmers','state');
INSERT INTO Scheme VALUES(437,3649,'14,000','farmers','state');
INSERT INTO Scheme VALUES(843,3937,'13,904','farmers','central');


DROP TABLE IF EXISTS Farming;
CREATE TABLE Farming (
  F_Aadhar_no BIGINT NOT NULL,
  Land_reg_num BIGINT NOT NULL,
  crop_id BIGINT NOT NULL,
  PRIMARY KEY (F_Aadhar_no,Land_reg_num,crop_id)
);

INSERT INTO Farming VALUES(783425631893,803405103,474);
INSERT INTO Farming VALUES(923704280464,419416173,784);
INSERT INTO Farming VALUES(410925727215,804429024,718);
INSERT INTO Farming VALUES(392087826186,953991701,037);
INSERT INTO Farming VALUES(194464669282,044833266,384);


DROP TABLE IF EXISTS Market;
CREATE TABLE Market(
  market_id INT NOT NULL,
  pincode BIGINT,
  state varchar(50),
  market_name varchar(50),
 country varchar(50),
  village_name varchar(50),
   PRIMARY KEY (market_id)

);

INSERT INTO Market VALUES(88357,539732,'Andra pradesh','star market','india','kodumur');
INSERT INTO Market VALUES(84759,583984,'telangana','vishal market','indial','chukkulu');
INSERT INTO Market VALUES(46887,593790,'tripura','lalitha market','india','kavali');
INSERT INTO Market VALUES(84373,598379,'rajasthan','abc market','india','lakkavaram');
INSERT INTO Market VALUES(87748,537433,'gujarat','xyz market','india','bhimavaram');



DROP TABLE IF EXISTS loan;
CREATE TABLE loan (
loan_id BIGINT NOT NULL,
 bank_namevar varchar(50),
  F_Aadharcard_no BIGINT,
  amount float,
  rateofinterest float,
  banknumber BIGINT,
   PRIMARY KEY (loan_id)
);

INSERT INTO loan VALUES(669437,'Andhra bank',783425631893,75000.00,2.5,2367);
INSERT INTO loan VALUES(669438,'Canara bank',923704280464,15000.00,2.5,2367);
INSERT INTO loan VALUES(669439,'Andhra bank',410925727215,35000.00,2.5,2367);
INSERT INTO loan VALUES(669537,'sbi bank',392087826186,5000.00,2.5,2367);
INSERT INTO loan VALUES(669468,'Andhra bank',194464669282,115000.00,2.5,2367);

DROP TABLE IF EXISTS crop;
CREATE TABLE crop (
crop_id BIGINT NOT NULL,
season varchar(50),
crop_worth float,
profit float,
PRIMARY KEY (crop_id)
);


INSERT INTO crop VALUES(474,'summer',10000,3000);
INSERT INTO crop VALUES(784,'rainy',20000,8000);
INSERT INTO crop VALUES(718,'summer',3500,1200);
