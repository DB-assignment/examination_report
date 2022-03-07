from flask import Flask, render_template, request, redirect, jsonify, flash
from flask_mysqldb import MySQL
import pymysql.cursors

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    user_name = request.form['user_name']
    password = request.form['password']
    get_tus_user(user_name, password)
    return render_template('login.html')


def get_tus_user(username, password):
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root1234',
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
