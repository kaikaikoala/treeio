from flask import Flask, request
from flaskext.mysql import MySQL
application = Flask(__name__)
mysql = MySQL()
application.config['MYSQL_DATABASE_DB'] = "treeio"
application.config['MYSQL_DATABASE_HOST'] = "localhost"
application.config['MYSQL_DATABASE_USER'] = "root"
application.config['MYSQL_DATABASE_PASSWORD'] = "password"
mysql.init_app(application)

@application.route("/")
def index():
    return application.send_static_file("index.html")

if __name__ == "__main__":
    application.debug=True
    application.run()