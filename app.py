from flask import Flask, redirect, render_template
from flask import url_for
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector


app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True


from pages.home_page.home_page import home_page
app.register_blueprint(home_page)

from pages.contactus.contactus import contactus
app.register_blueprint(contactus)

from pages.assignment3_1.assignment3_1 import assignment3_1
app.register_blueprint(assignment3_1)

from pages.assignment3_2.assignment3_2 import assignment3_2
app.register_blueprint(assignment3_2)

from pages.assignment_4.assignment_4 import assignment_4
app.register_blueprint(assignment_4)


if __name__ == '__main__':
    app.run(debug=True)
