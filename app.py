import pandas as pd
import json

from flask import Flask, render_template, request, redirect, jsonify, flash
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from collections import OrderedDict
from service.user import get_user, insert_users_service, get_permission, get_user_percentage_data
from flask_paginate import Pagination, get_page_parameter, get_page_args
import pymysql.cursors

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root1234'  # root1234
app.config['MYSQL_DB'] = 'assignment_db'
pageLimit = 10
mysql = MySQL(app)


@app.route('/new_user')
def add_user_view():
    return render_template('register.html')


@app.route('/register', methods=['post'])
def add_user():
    conn = None
    cursor = None
    try:
        details = request.form
        first_name = details['first_name']
        last_name = details['last_name']
        email = details['email']
        password = details['password']
        # validate the received values
        if first_name and last_name and email and request.method == 'POST':
            # save edits
            sql = "INSERT INTO tus_user(first_name, last_name, email, password) VALUES(%s, %s, %s, %s)"
            data = (first_name, last_name, email, password)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            response = jsonify(message='User added successfully.', id=cursor.lastrowid)
            # response.data = cursor.lastrowid
            response.status_code = 200
            flash('User added successfully!')
            return redirect('/home')
        else:
            return 'Error while adding user'
    except Exception as e:
        print(e)
        response = jsonify('Failed to add user.')
        response.status_code = 400
    finally:
        cursor.close()
        conn.close()
        return (response)


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


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/go_to_login')
def go_to_login():
    return render_template('login.html')


@app.route('/go_to_register')
def go_to_register():
    return render_template('register.html')


@app.route('/login', methods=['POST'])
def login():
    user_name = request.form['user_name']
    password = request.form['password']
    users = get_user(mysql, password, user_name)
    if len(users) > 0:
        user = users[0]

    user_id = user["user_id"]
    # permissions = get_permission(mysql, user_id)
    msg = "username or password is wrong"
    return redirect("/users")


@app.route('/users', methods=['GET'])
def users():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    offset = str((page - 1) * 10)
    cur = mysql.connection.cursor()
    sql = "SELECT * FROM assignment_db.tus_user order by user_id desc;"
    cur.execute(sql)
    row_headers = [x[0] for x in cur.description]
    users = cur.fetchall()
    pagination = Pagination(page=page, per_page=per_page, total=len(users))
    user_count = len(users)
    # json_data = []
    # for result in rv:
    #     json_data.append(dict(zip(row_headers, result)))

    #
    sql = "SELECT * FROM assignment_db.tus_user limit 10 OFFSET " + offset + ";"
    cur.execute(sql)
    row_headers = [x[0] for x in cur.description]
    rv2 = cur.fetchall()
    pagination_users = rv2
    description = cur.description
    cur.close()

    user_percentage_data = get_user_percentage_data(mysql, users, description)
    print()

    s_role_type = []
    percentage = []
    for user in user_percentage_data:
        role_type = user["role_type"]
        count = user["count"]
        percentage.append(round(count / user_count * 100, 2))
        s_role_type.append(role_type)

    user_percentage_pie_data = pd.DataFrame(
        OrderedDict({'type': pd.Series(s_role_type), 'percentage': pd.Series(percentage)})).to_json(
        orient="records")

    user_percentage_pie_data = json.loads(user_percentage_pie_data)
    for x in user_percentage_pie_data:
        print(x)


    return render_template('user.html', users=pagination_users, per_page=per_page, rv=rv2, pagination=pagination,
                           user_percentage_pie_data=user_percentage_pie_data)


@app.route('/insert_users', methods=['GET'])
def insert_users():
    insert_users_service(mysql)
    return "1"


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
