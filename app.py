import pandas as pd
import json

from flask import Flask, render_template, request, redirect, jsonify, flash, url_for
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from collections import OrderedDict

from sqlalchemy import true

from service.user import get_user, insert_users_service, get_permission, get_user_percentage_data, validateUser, \
    get_role, get_lecture_student_grades, get_lecture_student_grades_rs, get_module_name, get_student_grades, \
    update_grade, save_user

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


@app.route('/register', methods=['POST'])
def register():
    user_name = request.form['user_name']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    save_user(mysql, user_name, first_name, last_name, email, password)

    # return redirect("/users")
    return render_template('home.html')

db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin@127.0.0.1/assignment-db"


# basic model
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'


@app.route('/error')
def error_handle(e):
    return e


if __name__ == '__main__':
    app.run()


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/')
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
    permissions = get_permission(mysql, user_id)
    roles = get_role(mysql, user_id)
    role_type = roles[0].get("role_type")

    if role_type == "admin":
        return redirect(url_for('.users', user_name=user_name, password=password))
    elif role_type == "lecturer":
        return redirect(url_for('.lecturer', user_name=user_name, password=password))
    else:
        return redirect(url_for('.student', user_name=user_name, password=password))

    msg = "username or password is wrong"

    # return redirect("/users")
    return render_template('home.html')
    # return render_template('user.html', user_name=user_name, user=user)


@app.route('/users', methods=['GET'])
def users():
    user_name = request.args['user_name']
    password = request.args['password']
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
                           user_percentage_pie_data=user_percentage_pie_data,user_name=user_name.capitalize())


@app.route('/insert_users', methods=['GET'])
def insert_users():
    insert_users_service(mysql)
    return "1"


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     first_name = request.form['first_name']
#     last_name = request.form['last_name']
#     reg_email = request.form['reg_email']
#     pwd = request.form['pwd']
#     print(first_name, last_name, reg_email, pwd)
#     register_tus_user(first_name, last_name, reg_email, pwd)
#     return render_template('register.html')


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


@app.route('/lecturer', methods=['GET', 'POST'])
def lecturer():
    user_name = request.args['user_name']
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    offset = str((page - 1) * 10)

    student_grades = get_lecture_student_grades(mysql, user_name, 0, offset)
    pagination = Pagination(page=page, per_page=per_page, total=len(student_grades))
    # pagination = Pagination(page=page, per_page=per_page, total=len(users))
    rv = get_lecture_student_grades_rs(mysql, user_name, 10, offset)

    module_name = get_module_name(mysql, user_name)
    module_name = module_name[0]
    return render_template('lecturer_info.html', student_grades=student_grades, pagination=pagination, rv=rv,
                           module_name=module_name, user_name=user_name.capitalize())


@app.route('/student', methods=['GET', 'POST'])
def student():
    user_name = request.args['user_name']
    student_grades = get_student_grades(mysql, user_name)
    # student_grades = get_student_grades(mysql, user_name)
    return render_template('student_info.html', user_name=user_name.capitalize(), student_grades=student_grades)


@app.route('/grade', methods=['GET', 'POST'])
def grade():
    grade_id = request.form['grade_id']
    assessment_mark = request.form['assessment_mark']
    exam_mark = request.form['exam_mark']
    final_exam = int(assessment_mark) + int(exam_mark)
    update_grade(mysql, grade_id, assessment_mark, exam_mark, str(final_exam))
    print()
    return "success"
