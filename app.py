from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import os
 
app = Flask(__name__)
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password! try again')
    return home()

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    age = TextField('Age:', validators=[validators.required()])
    address = TextField('Address:', validators=[validators.required()])
    eid = TextField('Email ID:', validators=[validators.required()])
    mobile = TextField('Mobile:', validators=[validators.required()])
    bg = TextField('Blood Group:', validators=[validators.required()])
    gen = TextField('Gender:', validators=[validators.required()])

@app.route("/form", methods=['GET', 'POST'])
def form():
    form = ReusableForm(request.form)
 
    print (form.errors)
    if request.method == 'POST':
        name=request.form['name']
        age=request.form['age']
        address=request.form['address']
        eid=request.form['eid']
        mobile=request.form['mobile']
        bg=request.form['bg']
        gen=request.form['gen']

        print (name, age, address, eid, mobile, bg, gen)
 
        if form.validate():
            # Save the comment here.
            flash('Hello ' + name + ', your data is saved!')
        else:
            flash('All the form fields are required. ')
 
    return render_template('form.html', form=form)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route('/doc', methods=['POST','GET'])
def doct():
    return render_template('doctable.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)