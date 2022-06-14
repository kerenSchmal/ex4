from flask import Flask, redirect, render_template
from flask import url_for
from datetime import timedelta
from flask import request, session, jsonify


app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True



# root of our website
@app.route('/')
def main_func():
    return redirect(url_for('homepage_func'))


@app.route('/contact')
def contact_func():
    return render_template('contact.html')


@app.route('/home page')
def homepage_func():
    return render_template('home page.html')


@app.route('/assignment3_2', methods=['GET', 'POST'])
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
                                       message='User not found.')

    return render_template('assignment3_2.html')


@app.route('/assignment3_1')
def assignment3_1_func():
    actor_info = {'name': 'brad', 'second_name': 'piTT', 'living in': 'USA'}
    best_movies = ('Mr. & Mrs. Smith', 'Mr. & Mrs. Smith', 'Oceans Eleven', 'World War Z', 'helma & Louise',
                   'the curious Case of Benjamin Button', 'Deadpool', 'Deadpool')
    awards = (
        'academy Awards', 'prime-time Emmy Award', 'Golden Globe Awards', 'briTIsh Academy Film Awards',
        'academy Awards')
    return render_template('assignment3_1.html', actor_info=actor_info, best_movies=best_movies, awards=awards)


@app.route('/log_out')
def logout_func():
    session['userIn'] = False
    session.clear()
    return redirect(url_for('assignment3_2_func'))


@app.route('/session')
def session_func():
    # print(session['CHECK'])
    return jsonify(dict(session))


userDict = {
    'shachar': ['shachar@gmail.com', 'fbnirb'],
    'ido123': ['ido123@gmail.com', 'f45903'],
    'oren': ['oren@gmail.com', 'g49902'],
    'yael': ['yael@gmail.com', 'tryyyy'],
    'noali': ['noali@gmail.com', 'v4kipkt'],
    'gilevi': ['gilevi@gmail.com', 'g4ijgi4']
}

if __name__ == '__main__':
    app.run(debug=True)
