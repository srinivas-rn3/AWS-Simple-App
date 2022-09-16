from os import environ
import pymysql
from flask import Flask
import socket
import time
from flask import request
from flask import jsonify

app = Flask(__name__)

# Connection parameters and access credentials
ipaddress   = environ.get('DB_HOST')
usr         = environ.get('DB_USER')
passwd      = environ.get('DB_PASS')
charset     = "utf8mb4"
curtype    = pymysql.cursors.DictCursor

def getDatabaseConnection(ipaddress, usr, passwd, charset, curtype):
    sqlCon  = pymysql.connect(host=ipaddress, user=usr, password=passwd, charset=charset, cursorclass=curtype);
    return sqlCon

# Define a method to create MySQL users
def createUser(cursor, userName, password, gender,
               querynum=0, 
               updatenum=0, 
               connection_num=0):
    try:
        sqlCreateUser = "INSERT INTO newdb.USER_DETAILS VALUES ('%s', '%s', '%s');" %(userName, password, gender)
        cursor.execute(sqlCreateUser)
    except Exception as Ex:
        print("Error creating MySQL User: %s"%(Ex))

# Method for listing users
def listUsers(cursor,
              querynum=0,
              updatenum=0,
              connection_num=0):
    try:
        sqlListUser = "SELECT * FROM newdb.USER_DETAILS"
        cursor.execute(sqlListUser)
        return cursor.fetchall()
    except Exception as Ex:
        print("Error creating MySQL User: %s"%(Ex))
    
@app.route('/app1/createuser')
def createuser():
	userName = request.args.get('user', default = 'myusername', type = str)
	password = request.args.get('pass', default = 'mypassword', type = str)
	gender = request.args.get('gender', default = 'male', type = str)
	mySQLConnection = getDatabaseConnection(ipaddress, usr, passwd, charset, curtype)
	mySQLCursor     = mySQLConnection.cursor()

	createUser(mySQLCursor, userName, password, gender)
	mySQLConnection.commit()
	return "<h1> user %s added successfully</h1>" %userName

@app.route('/app1/listuser')
def listuser():
	mySQLConnection = getDatabaseConnection(ipaddress, usr, passwd, charset, curtype)
	mySQLCursor     = mySQLConnection.cursor()
	return jsonify(listUsers(mySQLCursor)) 


@app.route('/app1/health')
def healthcheck():
	return "<h1>App1 is healthy</h1>"
	
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
