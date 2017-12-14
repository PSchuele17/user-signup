from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('user-signup.html')


@app.route("/signup")
def display_signup():

    return render_template('user-signup.html')

@app.route("/signup", methods=['POST'])
def signup():


    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = 'passwords need to match'
    email_error = ''

    if len(username) < 3 or len(username) > 20:
        username_error ="That's not a valid username"
        
    elif " " in username:
        username_error ="That's not a valid username"

    if len(password) < 3 or len(password) > 20:
        password_error ="That's not a valid password"
        
    elif " " in password:
        password_error ="That's not a valid password"

    if  verify == password:
        verify_error=""
    
    if len(email) < 3 or len(email) > 20:
        email_error ="That's not a valid email"

    elif " " in email:
        email_error ="That's not a valid email"
        
    elif  "@" not in email and "." not in email:
        email_error ="That's not a valid email"

        
    if not username_error and not password_error and not verify_error:
        return render_template("success.html",
            username=username)
    else:
        return render_template("user-signup.html",
            username=username,
            username_error=username_error,
            password_error=password_error,
            verify_error=verify_error,
            email=email,
            email_error=email_error)

"""def success_validate():
    if password == verify and not email_error and not username_error:
        return render_template('success.html')
    else:
        return render_template('user-signup.html',
        username=username,
        email=email)
"""



app.run()