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
application.config['SECRET_KEY'] = "dotslashwootyay"
mysql.init_app(application)



@application.route("/")
def index():
    return application.send_static_file("index.html")

@application.route ("/organizationPortal/<organization>")
def organizationPortal(organization):
    if session['logged_in'] == False:
        return redirect("/orgLogin")
    print ("organizations/"+organization+"/orgPortal.html")
    return application.send_static_file("organizations/"+organization+"/orgPortal.html")

@application.route ("/memberPortal/<organization>/<member>")
def memberPortal(organization,member):
    return application.send_static_file("/static/organizations/"+str(organization)+"/"+str(member)+".html")

@application.route("/orgSignUp")
def orgSignUp():
    return application.send_static_file("orgSignUp.html")

@application.route("/SignUp")
def memSignUp():
    return application.send_static_file("SignUp.html")

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
    return redirect("/orgLogin")

@application.route("/orgLogin")
def orgLogin():
    return application.send_static_file("orgLogin.html")

@application.route("/login/<what>", methods = ["POST"])
def login(what):
    try:
        uname = str(request.form['e'])
        password = hashlib.sha224(request.form['p'].encode('utf-8')).hexdigest()
    except:
        return redirect("/"+str(what)+"Login")
    session['logged_in'] = create.checkLogin(uname,password,what,mysql)
    if session['logged_in']:
        if str(what)== "org":
            return redirect ("/organizationPortal/ohlone")
        elif str(what)=="mem":
            return redirect("/memberPortal")
    return redirect("/"+str(what)+"Login")



if __name__ == "__main__":
    application.debug=True
    application.run()