from flask import Flask, render_template, request
import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'appdb'
username = 'postgres'
pwd = 'cs425'
port_id = 5432
conn = None
cur = None


app = Flask(__name__)

def fetch(table, query):
    try:
        conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(query)
        data = cur.fetchall()
        conn.commit() 
        cur.close()
        conn.close()
        return data
    except (Exception, psycopg2.Error) as error:
        print("Failed" + table + " table:", error)

def change(table, query, value):
    try:
        conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(query, value)
        conn.commit() 
        cur.close()
        conn.close()
    except (Exception, psycopg2.Error) as error:
        print("Failed" + table + " table:", error)


@app.route('/',methods = ["POST", "GET"])
def index():
    return render_template('index.html')

@app.route('/customerLogin',methods = ["POST", "GET"])
def customerLogin():
    return render_template('customerSignIn.html')

@app.route('/employeeLogin',methods = ["POST", "GET"])
def employeeLogin():
    return render_template('employeeSelection.html')

@app.route('/managerSignIn',methods = ["POST", "GET"])
def managerSignIn():
    return render_template('managerSignIn.html')

@app.route('/loanspecialistSignIn',methods = ["POST", "GET"])
def loanspecialistSignIn():
    return render_template('loanspecialistSignIn.html')

@app.route('/tellerSignIn',methods = ["POST", "GET"])
def tellerSignIn():
    return render_template('tellerSignIn.html')

@app.route('/customerHP',methods = ["POST", "GET"])
def customerHP():
    ssn = request.form.to_dict()
    custssn = ssn["ssnlogin"]
    table = 'CUSTOMER'
    query = f"""SELECT name FROM CUSTOMER WHERE ssn = '{custssn}'"""
    name = fetch(table, query)
    table1 = 'CUSTOMER'
    query1 = f"""SELECT address FROM CUSTOMER WHERE ssn = '{custssn}'"""
    address = fetch(table1, query1)
    return render_template('customerHP.html', ssn = custssn, name = name[0][0], address = address[0][0])

@app.route('/tellerHP',methods = ["POST", "GET"])
def tellerHP():
    ssn = request.form.to_dict()
    tellssn = ssn["ssnlogin"]
    return render_template('tellerHP.html', ssn = tellssn)

@app.route('/managerHP',methods = ["POST", "GET"])
def managerHP():
    ssn = request.form.to_dict()
    custssn = ssn["ssnlogin"]
    return render_template('managerHP.html', ssn = custssn)



if __name__ == "__main__":
    app.run(debug=True)

