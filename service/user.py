from flask import json


def get_user(mysql, password, user_name):
    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT * FROM assignment_db.tus_user where user_name='" + user_name + "' and password='" + password + "';")
    row_headers = [x[0] for x in cur.description]  # this will extract row headers
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return json.dumps(json_data)
