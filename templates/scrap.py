else:
        return render_template('user-signup.html',
        username=username,
        email=email)

@app.route("/signup", methods=['POST'])
def signup():

 if password == verify and not email_error and not username_error:
        return render_template('success.html')
    else:
        return render_template('user-signup.html',
        username=username,
        email=email)