from flask import Flask, render_template
import constant as cst
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = cst.MYSQL_HOST
app.config['MYSQL_USER'] = cst.MYSQL_USER
app.config['MYSQL_PASSWORD'] = cst.MYSQL_PASSWORD
app.config['MYSQL_DB'] = cst.MYSQL_DB

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def error_page(e):
    return render_template('404.html', title= "Not Found"), 404


@app.errorhandler(500)
def error_page(e):
    return render_template('500.html', title= "Server Error"), 500


if __name__ == '__main__':
    app.run(debug=True)
