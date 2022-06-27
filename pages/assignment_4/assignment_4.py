import requests as requests
from flask import redirect, render_template, Blueprint
from flask import url_for
from flask import request, session, jsonify
import mysql.connector


assignment_4 = Blueprint('assignment_4', __name__, static_folder='static',
                         static_url_path='/pages/assignment_4',
                         template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='mydata')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@assignment_4.route('/assignment_4')
def assignment_4_func():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment_4.html', users=users_list)


@assignment_4.route('/insert_user', methods=['POST'])
def insert_user_func():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    if check_if_letters(username) == True:

        for user in users_list:
            if username == user.username:
                return render_template('assignment_4.html', users=users_list, message="user already exists")
        query = "INSERT INTO users(username, email, password) VALUES ('%s', '%s', '%s')" % (username, email, password)
        interact_db(query=query, query_type='commit')
        query = 'select * from users'
        users_list = interact_db(query, query_type='fetch')
        return render_template('assignment_4.html', users=users_list, message="User successfully added")
    else:
        return render_template('assignment_4.html', users=users_list, message="Username can include only LETTERS")


@assignment_4.route('/delete_user', methods=['POST'])
def delete_user():
    username = request.form['username']
    query = 'select * from users'
    users = interact_db(query, query_type='fetch')
    for user in users:
        if username == user.username:
            query = "DELETE FROM users WHERE username='%s';" % username
            interact_db(query, query_type='commit')
            query = 'select * from users'
            users = interact_db(query, query_type='fetch')
            return render_template('assignment_4.html',
                                   message='User successfully deleted', users=users)
    return render_template('assignment_4.html',
                           message='User not found', users=users)



@assignment_4.route('/update_user', methods=['POST'])
def update_user():
    username = request.form['username']
    email= request.form['email']
    password = request.form['password']
    query = 'select * from users'
    users = interact_db(query, query_type='fetch')
    for user in users:
        if username == user.username:

            query ="UPDATE users SET email='%s', password='%s' WHERE username = '%s';" % (email, password, username)
            interact_db(query, query_type='commit')
            query = 'select * from users'
            users = interact_db(query, query_type='fetch')
            return render_template('assignment_4.html',
                                   message='User successfully updated', users=users)
    return render_template('assignment_4.html',
                           message='User not found', users=users)


@assignment_4.route('/assignment4/users')
def go_to_assignment_4_jasonify():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return jsonify(users_list)


@assignment_4.route('/assignment_4/outer_source')
def go_to_assignment_4_outer_source():
    user_id = request.args['user_id']
    response = requests.get(url=f"https://reqres.in/api/users/{user_id}")
    user = response.json()
    session['user'] = user.get('data')
    return redirect(url_for('assignment_4.assignment_4_func'))

@assignment_4.route('/assignment_4/clear')
def clear_backend():
    session['user'] = None
    return redirect(url_for('assignment_4.assignment_4_func'))


def check_if_letters(string):
    for i in string:
        if i < 'A' or i > 'z' or (i > 'Z' and i < 'a'):
            return False
    return True


def check_if_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


@assignment_4.route('/assignment4/restapi_users', defaults={'USER_ID': 1}, methods=['GET'])
@assignment_4.route('/assignment4/restapi_users/<USER_ID>', methods=['GET'])
def get_restapi_users(USER_ID):
    if check_if_integer(USER_ID):
        response = requests.get(f'https://reqres.in/api/users/{USER_ID}')
        if response.status_code == 200:
            users = response.json()
            return users.get('data')
        else:
            message = "User doesn't exist"
            return jsonify(message)
    else:
        message = "please insert only INTEGER"
        return jsonify(message)



