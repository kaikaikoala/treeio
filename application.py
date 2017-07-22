from flask import Flask, request, session, redirect, url_for
from flaskext.mysql import MySQL
import create
import os
from flask_login import LoginManager
#from flask_bcrypt import generate_password_hash, check_password_hash
import user

application = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(application)
mysql = MySQL()
application.config['MYSQL_DATABASE_DB'] = "TreeIO" ###KEEP THIS THE SAME###
application.config['MYSQL_DATABASE_HOST'] = "localhost" #change this for your computer/server
application.config['MYSQL_DATABASE_USER'] = "root" #change this for your computer/server
#application.config['MYSQL_DATABASE_PASSWORD'] = "password" #change this for your computer/server
#application.config['SECRET_KEY'] = "dotslashwootyay"
mysql.init_app(application)


@application.route("/")
@application.route("/index")
def index():
    return application.send_static_file("main-site/index.html")

@application.route("/organize")
def orgSignUp():
    return application.send_static_file("main-site/organize.html")
    
    
@application.route("/sign-in")
def signIn():
    return application.send_static_file("main-site/sign-ins.html")
    
@application.route("/sign-up")
def signup():
    return application.send_static_file("main-site/sign-up.html")
    
@application.route("/findOrg")
def findOrg():
    return application.send_static_file("main-site/org-find.html")
    
@application.route("/login", methods=["POST"])
def login():
    #import pdb; pdb.set_trace()
    uname = request.form['username']
    password = hashlib.sha224(request.form['password'].encode('utf-8')).hexdigest()
    return "Logged In"
        
        
    
@application.route('/explore')
def explore():
    return application.send_static_file('main-site/explore.html')

"""
@application.route ("/organizationPortal/<organization>")
def organizationPortal(organization):
    if session['logged_in'] == False:
        return redirect("/orgLogin")
    print ("organizations/"+organization+"/orgPortal.html")
    return application.send_static_file("main-site/organizations/"+organization+"/orgPortal.html")

@application.route ("/memberPortal/<organization>/<member>")
def memberPortal(organization,member):
    return application.send_static_file("/main-site/organizations/"+str(organization)+"/"+str(member)+".html")




@application.route("/SignUp")
def memSignUp():
    return application.send_static_file("main-site/SignUp.html")

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
    return application.send_static_file("main-site/orgLogin.html")

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
"""


if __name__ == "__main__":
    application.debug=True
    application.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))