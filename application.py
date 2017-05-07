from flask import Flask, request
from flaskext.mysql import MySQL
application = Flask(__name__)
mysql = MySQL()
application.config['MYSQL_DATABASE_DB'] = "treeio"
application.config['MYSQL_DATABASE_HOST'] = "localhost"
application.config['MYSQL_DATABASE_USER'] = "root"
application.config['MYSQL_DATABASE_PASSWORD'] = "password"
mysql.init_app(application)
login_manager.init_app(app)

@application.route("/")
def index():
    return application.send_static_file("index.html")

@application.route("/orgsignup", methods=["POST"])
def orgSignUp():
    return application.send_static_file("orgSignUp.html")

@application.route("/orglogin", methods=["POST"])
def orgLogin():
    return application.send_static_file("orgLogin.html")

if __name__ == "__main__":
    application.debug=True
    application.run()