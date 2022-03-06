from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
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
            #response.data = cursor.lastrowid
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
        return(response)    

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
