from flask import Flask, render_template, request
from sign_up import login

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    form = render_template("signup.html")
    return form.format('','','','')

@app.route("/", methods= ['POST'])
def username():
    form = render_template("signup.html")
    user = request.form.get('username')
    passw = request.form.get('password')
    ver = request.form.get('verify')
    mail = request.form.get('email')
    uname = login(user, passw, ver, mail)
    return uname

app.run()