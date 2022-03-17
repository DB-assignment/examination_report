import json

from flask import Flask, render_template, request, redirect, jsonify, flash
from flask_mysqldb import MySQL
import pymysql.cursors
from models.tus_user import tus_user
from service.user import get_user, insert_users_service
from flask_paginate import Pagination, get_page_parameter, get_page_args

pageLimit = 10

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root1234'
app.config['MYSQL_DB'] = 'assignment_db'

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


@app.route('/login', methods=['POST'])
def login():
    user_name = request.form['user_name']
    password = request.form['password']
    users = get_user(mysql, password, user_name)
    if len(users) > 0:
        user = users[0]
    msg = "username or password is wrong"
    return render_template('user.html', user_name=user_name, user=user)


@app.route('/users', methods=['GET'])
def users():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    offset = str((page - 1) * 10)
    cur = mysql.connection.cursor()
    sql = "SELECT * FROM assignment_db.tus_user order by user_id desc;"
    cur.execute(sql)
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    pagination = Pagination(page=page, per_page=per_page, total=len(rv))
    # json_data = []
    # for result in rv:
    #     json_data.append(dict(zip(row_headers, result)))

    #
    sql = "SELECT * FROM assignment_db.tus_user limit 10 OFFSET " + offset + ";"
    cur.execute(sql)
    row_headers = [x[0] for x in cur.description]
    rv2 = cur.fetchall()
    pagination_users = rv2
    return render_template('user.html', users=pagination_users, per_page=per_page, rv=rv2, pagination=pagination)


@app.route('/insert_users', methods=['GET'])
def insert_users():
    insert_users_service(mysql)
    return "1"
