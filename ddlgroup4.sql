CREATE TABLE employee(
	ssn NUMERIC (9,0), 
	firstname varchar(30), 
	lastname varchar(30),  
	streenNum NUMERIC (4),
	streetName varchar(30) 
	city varchar(30),  
	zipcode NUMERIC (6), 
	state varchar(2),  
	emprole varchar (30)
	salary NUMERIC (10,2) DEFAULT=0, 
	BranchID int(5),
	PRIMARY key(ssn)
	
);     
CREATE ROLE manager; 
CREATE ROLE teller; 
CREATE ROLE loanSpecialist;   

CREATE TABLE customer(
	ssn NUMERIC (9,0), 
	firstname varchar(30), 
	lastname varchar(30),  
	streenNum NUMERIC (4),
	streetName varchar(30) 
	city varchar(30),  
	zipcode NUMERIC (6), 
	state varchar(2), 
	homebranchID int (5)
	PRIMARY key(ssn)
);   

CREATE TABLE Account(  
	accountID NUMERIC (15)  
	balance  NUMERIC (10,2), Check(Balance >0)
	accountType varchar(20)
	FOREIGN key(ssn)
	PRIMARY key(accountID)
);   

CREATE VIEW accountView AS 
SELECT balance 
FROM Account

GRANT SELECT,UPDATE ON accountView TO teller;  


CREATE TABLE Branch ( 
	ID int (5),
	Branchname varchar(30),  
	PRIMARY KEY (ID)
);
CREATE TABLE loans(
	loan_id int (8)   
	
	FOREIGN key(ssn)
	amount NUMERIC (10,2) CHECK (amount<0),  
	period int (10)   
	interestSchedule double (3)   
	PRIMARY key(loan_id)
);  

GRANT ALL ON loans TO manager; 
GRANT ALL ON Account TO manager; 
GRANT ALL  ON customer TO manager; 
GRANT ALL ON employee TO manager;

GRANT ALL ON loans TO loanSpecialist; 
GRANT ALL ON Account TO loanSpecialist; 
GRANT ALL  ON customer TO loanSpecialist;  

CREATE TABLE transac (
	id int(5);  
	occured date;  
	 t time;  
	t_type varchar(20);   
	amount NUMERIC (10,2)  
	PRIMARY KEY (id)
);
GRANT ALL ON transac TO manager;
GRANT ALL ON Branch TO manager;

