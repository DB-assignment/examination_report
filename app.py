from flask import Flask, render_template, request, redirect, jsonify, flash
# from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
import pymysql.cursors

app = Flask(__name__)

db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin@127.0.0.1/assignment-db"

# basic model
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/error')
def error_handle(e):
    return e


if __name__ == '__main__':
    app.run()


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/go_to_login')
def go_to_login():
    return render_template('login.html')

@app.route('/go_to_register')
def go_to_register():
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    user_name = request.form['user_name']
    password = request.form['password']
    get_tus_user(user_name, password)
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    reg_email = request.form['reg_email']
    pwd = request.form['pwd']
    print(first_name, last_name, reg_email, pwd)
    register_tus_user(first_name, last_name, reg_email, pwd)
    return render_template('register.html')


def register_tus_user(first_name, last_name, reg_email, pwd):
    print(first_name, last_name, reg_email, pwd)
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='admin',
        db='assignment_db'
    )

    cursor = connect.cursor()
    sql = "INSERT INTO assignment_db.tus_user (first_name, last_name, email, password) VALUES ('" + first_name + "', '" + last_name + "', '" + reg_email + "', '" + pwd + "');"
    cursor.execute(sql)
    connect.close()
    return True



def get_tus_user(username, password):
    print(username, password)
    connect = pymysql.Connect(
        #host='localhost',
        #port=3306,
        #user='root',
        #passwd='root1234',
        #db='assignment_db'
        host='localhost',
        port=3306,
        user='root',
        passwd='admin',
        db='assignment_db'
    )

    cursor = connect.cursor()
    sql = "SELECT * FROM assignment_db.tus_user where first_name='" + username + "' and password=" + password + "; "
    cursor.execute(sql)
    user = cursor.fetchall()
    print(user)
    # for row in cursor.fetchall():
    #     id = row[1]
    #     username = row[2]
    #     last_name = row[3]
    #     email = row[4]
    #     password = row[5]
    #     print(row)
    connect.close()
    return user
