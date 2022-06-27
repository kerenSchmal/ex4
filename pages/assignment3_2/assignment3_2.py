from flask import Flask, redirect, render_template, Blueprint
from flask import url_for
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector

assignment3_2 = Blueprint('assignment3_2', __name__, static_folder='static',
                          static_url_path='/pages/assignment3_2',
                          template_folder='templates')




@assignment3_2.route('/assignment3_2', methods=['GET', 'POST'])
def assignment3_2_func():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        session['username'] = username
        session['email'] = email
        session['password'] = password
        session['userIn'] = True
        return render_template('assignment3_2.html')

    if request.method == 'GET':
        if 'username-search' in request.args:
            username = request.args['username-search']
            if len(username) == 0:
                return render_template('assignment3_2.html',
                                       userDict=userDict)
            if username in userDict:
                return render_template('assignment3_2.html',
                                       Username=username,
                                       Email=userDict[username][0],
                                       Password=userDict[username][1])
            else:
                return render_template('assignment3_2.html',
                                       message='User not found')

    return render_template('assignment3_2.html')


@assignment3_2.route('/log_out')
def logout_func():
    session['userIn'] = False
    session.clear()
    return redirect(url_for('assignment3_2.assignment3_2_func'))


userDict = {
    'shachar': ['shachar@gmail.com', 'fbnirb'],
    'ido': ['ido123@gmail.com', 'f45903'],
    'oren': ['oren@gmail.com', 'g49902'],
    'yael': ['yael@gmail.com', 'tryyyy'],
    'noali': ['noali@gmail.com', 'v4kipkt'],
    'gilevi': ['gilevi@gmail.com', 'g4ijgi4']
}


@assignment3_2.route('/session')
def session_func():
    # print(session['CHECK'])
    return jsonify(dict(session))

