from flask import json
from collections import OrderedDict


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


def validateUser(mysql, user_id):
    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT * FROM assignment_db.user_role where user_id='" + user_id + ";")
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return json_data
    # user_id = users[0]['user_id']
    # user_role = validateUser(mysql, user_id)
    # if user_role[0][role_id] == '1':
    #     return render_template('users.html')
    # else:
    #     return render_template('home.html')


def get_permission(mysql, user_id):
    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT * FROM assignment_db.permission where permission_id in (SELECT permission_id FROM assignment_db.role_permission where role_id in (SELECT role_id FROM assignment_db.user_role where user_id in (" + str(
            user_id) + ")));")
    row_headers = [x[0] for x in cur.description]  # this will extract row headers
    rv = cur.fetchall()
    cur.close()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    # return json.dumps(json_data)
    return json_data


def get_role(mysql, user_id):
    cur = mysql.connection.cursor()
    sql = "SELECT user_role.user_id,role.role_type FROM assignment_db.user_role inner join assignment_db.role on user_role.role_id = role.role_id where user_id = " + str(
        user_id) + ";"
    cur.execute(sql)
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
        sql = "insert into assignment_db.tus_user values(" + id + ",'" + user_name + "','','','" + email + "','" + user_name + "')"
        print(sql)
        cur.execute(sql)
        mysql.connection.commit()


def get_user_percentage_data(mysql, data, description):
    json_data = []
    row_headers = [x[0] for x in description]
    for result in data:
        json_data.append(dict(zip(row_headers, result)))

    user_ids = ""
    for user in json_data:
        user_id = str(user["user_id"]) + ","
        user_ids += user_id
        # print(user_id)

    user_ids = user_ids[0:len(user_ids) - 1]

    cur = mysql.connection.cursor()
    sql = "select role_type,COUNT(role_type) count from (select role_type from (SELECT role_id FROM assignment_db.user_role where user_id in (" + user_ids + ")) as newRole INNER JOIN assignment_db.role ON newRole.role_id = assignment_db.role.role_id) as newtable group by role_type;"
    cur.execute(sql)

    json_data1 = []
    row_headers = [x[0] for x in cur.description]
    users = cur.fetchall()
    for result in users:
        json_data1.append(dict(zip(row_headers, result)))
    return json_data1


def get_lecture_student_grades(mysql, user_name, limit, offset):
    cur = mysql.connection.cursor()
    sql = "select newtable1.user_id,tus_user.first_name,tus_user.last_name,newtable1.grade_id,grade.assessment_mark,grade.exam_mark,grade.final_mark from(" \
          "SELECT * FROM assignment_db.user_module where module_id =(" \
          "SELECT module_id FROM assignment_db.user_module where user_id = (" \
          "select user_id from assignment_db.tus_user where user_name='" + user_name + "')) and grade_id !=0 )as newtable1 " \
                                                                                       "inner join assignment_db.grade on newtable1.grade_id = grade.grade_id inner join assignment_db.tus_user on newtable1.user_id = tus_user.user_id;"

    if int(offset) > 0 and int(limit) > 0:
        sql = sql + " limit " + limit + " OFFSET " + str(offset)
    # sql = sql + " limit "+limit+" OFFSET " + str(offset)
    cur.execute(sql)
    json_data = []
    row_headers = [x[0] for x in cur.description]
    users = cur.fetchall()
    for result in users:
        json_data.append(dict(zip(row_headers, result)))
    return json_data


def get_lecture_student_grades_rs(mysql, user_name, limit, offset):
    cur = mysql.connection.cursor()
    sql = "select newtable1.user_id,tus_user.first_name,tus_user.last_name,newtable1.grade_id,grade.assessment_mark,grade.exam_mark,grade.final_mark from(" \
          "SELECT * FROM assignment_db.user_module where module_id =(" \
          "SELECT module_id FROM assignment_db.user_module where user_id = (" \
          "select user_id from assignment_db.tus_user where user_name='" + user_name + "')) and grade_id !=0 )as newtable1 " \
                                                                                       "inner join assignment_db.grade on newtable1.grade_id = grade.grade_id inner join assignment_db.tus_user on newtable1.user_id = tus_user.user_id"

    sql = sql + " limit " + str(limit) + " OFFSET " + str(offset)

    print(sql)
    cur.execute(sql)
    rv = cur.fetchall()
    cur.close()
    return rv


def get_module_name(mysql, user_name):
    cur = mysql.connection.cursor()
    sql = "select t2.module_name from(SELECT * FROM assignment_db.user_module where user_id = (" \
          "select user_id from assignment_db.tus_user where user_name='" + user_name + "') and grade_id=0) as t1 " \
                                                                                       "inner join assignment_db.module t2 on t1.module_id = t2.module_id;"
    cur.execute(sql)
    rv = cur.fetchall()
    return rv


def get_student_grades(mysql, user_name):
    cur = mysql.connection.cursor()
    sql = "SELECT grade.grade_id,user_module.user_id,tus_user.first_name,tus_user.last_name,module.module_name,grade.assessment_mark,grade.exam_mark,grade.final_mark FROM assignment_db.user_module" + \
          " inner join assignment_db.grade" + \
          " on user_module.grade_id = grade.grade_id" + \
          " inner join assignment_db.tus_user" + \
          " on user_module.user_id = tus_user.user_id" + \
          " inner join assignment_db.module" + \
          " on user_module.module_id = module.module_id" + \
          " where user_module.user_id=(select user_id from assignment_db.tus_user where user_name ='" + user_name + "');"
    print(sql)
    cur.execute(sql)
    json_data = []
    row_headers = [x[0] for x in cur.description]
    users = cur.fetchall()
    for result in users:
        json_data.append(dict(zip(row_headers, result)))
    return json_data
