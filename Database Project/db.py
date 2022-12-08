import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'appdb'
username = 'postgres'
pwd = 'cs425'
port_id = 5432
conn = None
cur = None

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('DROP TABLE IF EXISTS customer')
    cur.execute('DROP TABLE IF EXISTS manager ')
    cur.execute('DROP TABLE IF EXISTS teller ')
    cur.execute('DROP TABLE IF EXISTS branch ')
    cur.execute('DROP TABLE IF EXISTS account ')
    cur.execute('DROP TABLE IF EXISTS transaction ')

    create_script = ''' CREATE TABLE IF NOT EXISTS customer (
                           id       int PRIMARY KEY,
                           name     varchar(40) NOT NULL,
                           address  varchar(40),
                           ssn      varchar(40),
                           branch   int 
    ) '''
    create_script1 = ''' CREATE TABLE IF NOT EXISTS manager (
                           id       int PRIMARY KEY,
                           name     varchar(40) NOT NULL,
                           address  varchar(40),
                           ssn      varchar(40),
                           branch   int,
                           salary   int 
    ) '''
    create_script2 = ''' CREATE TABLE IF NOT EXISTS teller (
                           id       int PRIMARY KEY,
                           name     varchar(40) NOT NULL,
                           address  varchar(40),
                           ssn      varchar(40),
                           branch   int,
                           salary   int
    ) '''
    create_script3 = ''' CREATE TABLE IF NOT EXISTS branch (
                           id       int PRIMARY KEY,
                           name     varchar(40) NOT NULL,
                           address  varchar(40),
                           branch   int 
    ) '''
    create_script4 = ''' CREATE TABLE IF NOT EXISTS account (
                           id       int PRIMARY KEY,
                           type     varchar(40) NOT NULL,
                           ssn      varchar(40),
                           balance  int,
                           accountnum   int
    ) '''
    create_script5 = ''' CREATE TABLE IF NOT EXISTS transaction (
                           id       int PRIMARY KEY,
                           fromacc   int,
                           type     varchar(40),
                           date     varchar(40),
                           amount   int,
                           toacc    int
    ) '''
    #Executes the creation of the tables to the database
    cur.execute(create_script)
    cur.execute(create_script1)
    cur.execute(create_script2)
    cur.execute(create_script3)
    cur.execute(create_script4)
    cur.execute(create_script5)

    #Inserting data into the tables
    insert_script = 'INSERT INTO customer (id, name, address, ssn, branch) VALUES (%s, %s, %s, %s, %s)'
    insert_values = [(1, 'Jack Timber', '456 S Clover Lane', '123456789', 5), (2, 'Bill Mason', '6789 W Jackson Blvd', '987654321', 6), (3, 'Mary Watkins', '3421 Elm Cir', '123498765', 5)]
    for record in insert_values:
        cur.execute(insert_script, record)

    insert_script1 = 'INSERT INTO manager (id, name, address, ssn, branch, salary) VALUES (%s, %s, %s, %s, %s, %s)'
    insert_values1 = [(1, 'James Franco', '4789 S Mary lane', '789090058', 5, 140000), (2, 'Billy Munson', '777 W 59th St', '675234332', 6, 120000)]
    for record in insert_values1:
        cur.execute(insert_script1, record)
    
    insert_script2 = 'INSERT INTO teller (id, name, address, ssn, branch, salary) VALUES (%s, %s, %s, %s, %s, %s)'
    insert_values2 = [(1, 'Tammy Duckworth', '123 W 67th St', '378291094', 5, 55000), (2, 'Mason Jarvis', '6012 W 59th St', '548309211', 6, 65000)]
    for record in insert_values2:
        cur.execute(insert_script2, record)
    
    insert_script3 = 'INSERT INTO branch (id, name, address, branch) VALUES (%s, %s, %s, %s)'
    insert_values3 = [(1, 'Northstar Plaza', '191 S Perry St', 5), (2, 'Hollywood Hills', '333 S Pleasent Dr', 6)]
    for record in insert_values3:
        cur.execute(insert_script3, record)
    
    insert_script4 = 'INSERT INTO account (id, type, ssn, balance, accountnum) VALUES (%s, %s, %s, %s, %s)'
    insert_values4 = [(1, 'Checking', '123456789', 67985, 1111), (2, 'Savings', '987654321', 562100, 2222), (3, 'Checking', '123498765', 1500, 3333)]
    for record in insert_values4:
        cur.execute(insert_script4, record)

    cur.execute("SELECT sum(balance) FROM ACCOUNT")
    data = cur.fetchall()
    print(data[0][0])
    conn.commit()


except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()