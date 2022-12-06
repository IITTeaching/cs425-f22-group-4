from flask import Flask, render_template, request


app = Flask(__name__)


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
    return render_template('customerHP.html')

if __name__ == "__main__":
    app.run(debug=True)