from flask import json


def get_user(mysql, password, user_name):
    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT * FROM assignment_db.tus_user where user_name='" + user_name + "' and password='" + password + "';")
    row_headers = [x[0] for x in cur.description]  # this will extract row headers
    rv = cur.fetchall()
    cur.close()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    # return json.dumps(json_data)
    return json_data


def get_users(mysql):
    cur = mysql.connection.cursor()
    cur.execute(
        # "SELECT * FROM assignment_db.tus_user;")
        "SELECT * FROM assignment_db.tus_user order by user_id desc limit 10;")
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return json_data


def insert_users_service(mysql):
    cur = mysql.connection.cursor()
    for x in range(1, 50):
        id = str(x + 1)
        user_name = "tom" + id
        email = user_name + "@gmail.com"
        sql = "insert into assignment_db.tus_user values("+id+",'"+user_name+"','','','"+email+"','"+user_name+"')"
        print(sql)
        cur.execute(sql)
        mysql.connection.commit()