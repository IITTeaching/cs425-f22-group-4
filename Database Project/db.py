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

    create_script = ''' CREATE TABLE IF NOT EXISTS customer (
                           id       int PRIMARY KEY,
                           name     varchar(40) NOT NULL,
                           address  varchar(40),
                           ssn      int,
                           branch   int 
    ) '''
    cur.execute(create_script)

    insert_script = 'INSERT INTO customer (id, name, address, ssn, branch) VALUES (%s, %s, %s, %s, %s)'
    insert_values = [(1, 'Jack Timber', '456 S Clover Lane', 123456789, 5), (2, 'Bill Mason', '6789 W Jackson Blvd', 987654321, 6), (3, 'Mary Watkins', '3421 Elm Cir', 123498765, 5)]
    for record in insert_values:
        cur.execute(insert_script, record)
    
    cur.execute('SELECT * FROM CUSTOMER')
    for record in cur.fetchall():
        print(record['ssn'], record['name'])
    conn.commit()

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()