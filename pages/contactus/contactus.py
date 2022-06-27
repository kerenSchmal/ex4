from flask import Flask, redirect, render_template, Blueprint
from flask import url_for
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector


contactus = Blueprint('contactus', __name__, static_folder='static',
                      static_url_path='/pages/contactus',
                      template_folder='templates')


@contactus.route('/contact')
def contact_func():
    return render_template('contact.html')


