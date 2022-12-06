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
    table2 = 'ACCOUNT'
    query2 = f"""SELECT balance FROM ACCOUNT WHERE ssn = '{custssn}'"""
    balance = fetch(table2, query2)
    table3 = 'ACCOUNT'
    query3 = f"""SELECT type FROM ACCOUNT WHERE ssn = '{custssn}'"""
    acctype = fetch(table3, query3)
    table4 = 'ACCOUNT'
    query4 = f"""SELECT accountnum FROM ACCOUNT WHERE ssn = '{custssn}'"""
    accountnum = fetch(table4, query4)
    return render_template('customerHP.html', ssn = custssn, name = name[0][0], address = address[0][0], balance = balance[0][0], type = acctype[0][0], accountnum = accountnum[0][0])

@app.route('/customerTransfer',methods = ["POST", "GET"])
def customerTransfer():
    return render_template('customerTransfer.html')

@app.route('/customerDelete',methods = ["POST", "GET"])
def customerDelete():
    return render_template('customerDelete.html')

@app.route('/customerDeleteSuccess',methods = ["POST", "GET"])
def customerDeleteSuccess():
    return render_template('customerDeleteSuccess.html')

@app.route('/customerTransferSuccess',methods = ["POST", "GET"])
def customerTransferSuccess():
    amount = request.form['amt']
    accountnumber = request.form['acct']
    return render_template('customerTransferSuccess.html', amount = amount, accountnumber = accountnumber)

#TELLER ACTIONS
@app.route('/tellerHP',methods = ["POST", "GET"])
def tellerHP():
    ssn = request.form.to_dict()
    tellssn = ssn["ssnlogin"]
    table = 'TELLER'
    query = f"""SELECT name FROM TELLER WHERE ssn = '{tellssn}'"""
    name = fetch(table, query)
    return render_template('tellerHP.html', ssn = tellssn, name = name[0][0])

#MANAGER ACTIONS
@app.route('/managerHP',methods = ["POST", "GET"])
def managerHP():
    ssn = request.form.to_dict()
    manssn = ssn["ssnlogin"]
    table = 'MANAGER'
    query = f"""SELECT name FROM MANAGER WHERE ssn = '{manssn}'"""
    name = fetch(table, query)
    return render_template('managerHP.html', ssn = manssn, name = name[0][0])

@app.route('/employeeLookup',methods = ["POST", "GET"])
def employeeLookup():
    return render_template('employeeLookup.html')

@app.route('/employeeLookupSuccess',methods = ["POST", "GET"])
def employeeLookupSuccess():
    empname = request.form.to_dict()
    employeename = empname['empname']
    table = 'TELLER'
    query = f"""SELECT ssn FROM TELLER WHERE name = '{employeename}'"""
    ssn = fetch(table, query)
    table1 = 'TELLER'
    query1 = f"""SELECT address FROM TELLER WHERE name = '{employeename}'"""
    address = fetch(table1, query1)
    return render_template('employeeLookupSuccess.html', ssn = ssn[0][0], address = address[0][0])

@app.route('/branchLookup',methods = ["POST", "GET"])
def branchLookup():
    return render_template('branchLookup.html')

@app.route('/customerLookup',methods = ["POST", "GET"])
def customerLookup():
    return render_template('customerLookup.html')

@app.route('/customerLookupSuccess',methods = ["POST", "GET"])
def customerLookupSuccess():
    custname = request.form.to_dict()
    customername = custname['custname']
    table = 'CUSTOMER'
    query = f"""SELECT ssn FROM CUSTOMER WHERE name = '{customername}'"""
    ssn = fetch(table, query)
    table1 = 'CUSTOMER'
    query1 = f"""SELECT address FROM CUSTOMER WHERE name = '{customername}'"""
    address = fetch(table1, query1)
    table2 = 'ACCOUNT'
    query2 = f"""SELECT accountnum FROM ACCOUNT WHERE ssn = '{ssn[0][0]}'"""
    accountnum = fetch(table2, query2)
    return render_template('customerLookupSuccess.html', ssn = ssn[0][0], address = address[0][0], accountnum = accountnum[0][0])

@app.route('/accountsWorth',methods = ["POST", "GET"])
def accountsWorth():
    return render_template('accountsWorth.html')

@app.route('/managerDeposit',methods = ["POST", "GET"])
def managerDeposit():
    return render_template('managerDeposit.html')

@app.route('/managerWithdrawal',methods = ["POST", "GET"])
def managerWithdrawal():
    return render_template('managerWithdrawal.html')

if __name__ == "__main__":
    app.run(debug=True)

