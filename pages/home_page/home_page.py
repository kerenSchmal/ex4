from flask import Flask, redirect, render_template, Blueprint
from flask import url_for
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector

home_page = Blueprint('home_page', __name__, static_folder='static',
                      static_url_path='/home_page',
                      template_folder='templates')


# root of our website
@home_page.route('/')
def main_func():
    return redirect(url_for('home_page.homepage_func'))


@home_page.route('/home page')
def homepage_func():
    return render_template('home page.html')


