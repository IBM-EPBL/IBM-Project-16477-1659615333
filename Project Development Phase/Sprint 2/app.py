from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField, IntegerField
import ibm_db
from passlib.hash import sha256_crypt
from functools import wraps

from sendgrid import *

#creating an app instance
app = Flask(__name__)

app.secret_key='a'

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=IBM_HOST;PORT=IBM_PORT;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=USERNAME;PWD=PASSWORD;",'','')
#Index
@app.route('/')
def index():
    return render_template('home.html')

#Products
@app.route('/products')
def products():
   return render_template('products.html')

#Locations
@app.route('/locations')
def locations():
    return render_template('locations.html')

#Product Movements
@app.route('/product_movements')
def product_movements():
   return render_template('product_movements.html')


#user register
@app.route('/register', methods=['GET','POST'])
def register():
        return render_template('register.html')


#User login
@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('login.html')

#Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash("You are now logged out", "success")
    return redirect(url_for('login'))

#Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
        return render_template('dashboard.html')


#Add Product
@app.route('/add_product', methods=['GET', 'POST'])
@is_logged_in
def add_product():
        return render_template('add_product.html')




#Add Location
@app.route('/add_location', methods=['GET', 'POST'])
@is_logged_in
def add_location():
  return render_template('add_location.html', form=form)





#Add Product Movement
@app.route('/add_product_movements', methods=['GET', 'POST'])
@is_logged_in
def add_product_movements():
    
    return render_template('add_product_movements.html', form=form)



if __name__ == '__main__':
    app.secret_key = "secret123"
    #when the debug mode is on, we do not need to restart the server again and again
    app.run(debug=True)
