from flask import Flask, request, session, redirect
from flaskext.mysql import MySQL
import create
import hashlib

application = Flask(__name__)
mysql = MySQL()
application.config['MYSQL_DATABASE_DB'] = "treeio" ###KEEP THIS THE SAME###
application.config['MYSQL_DATABASE_HOST'] = "localhost" #change this for your computer/server
application.config['MYSQL_DATABASE_USER'] = "root" #change this for your computer/server
application.config['MYSQL_DATABASE_PASSWORD'] = "password" #change this for your computer/server
mysql.init_app(application)



@application.route("/")
def index():
    return application.send_static_file("index.html")


@application.route ("/organizationPortal", subdomain="<organization>")
def organizationPortal(organization):
    return application.send_static_file("/static/"+organization+"/orgPortal.html")


@application.route("/orgSignUp")
def orgSignUp():
    return application.send_static_file("orgSignUp.html")

@application.route("/signUpProcess/<which>",methods=["POST"])
def signUpProcess(which):
    info = {}
    info['name'] = request.form['schoolname']
    info['shortname'] = request.form['shortname']
    info['email'] = request.form['email']
    info['password'] = hashlib.sha224(request.form['password'].encode('utf-8')).hexdigest()
    print (which)
    if str(which)=="org":
        info['city'] = request.form['city']
        info['state'] = request.form['state']
        info['zipcode'] = request.form['zipcode']
    else:
        info['school'] = request.form['school']
    create.createEntry(info,str(which),mysql)
    return redirect("/")

@application.route("/orgLogin", methods=["POST"])
def orgLogin():
    return application.send_static_file("orgLogin.html")

@application.route("/login/org", methods = ["POST"])
def loginOrg():
    uname = request.form['email']
    password = hashlib.sha224(request.form['password'].encode('utf-8')).hexdigest()
    session['logged_in'] = checkLogin(uname,password)
    if session['logged_in']:
        return redirect ("/organizationPortal")

if __name__ == "__main__":
    application.debug=True
    application.run()