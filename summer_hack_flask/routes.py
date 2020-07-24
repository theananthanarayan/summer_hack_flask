
from flask import Flask, render_template, session, request, jsonify, Response, flash, redirect, url_for
from summer_hack_flask import app, bcrypt, db
from summer_hack_flask.forms import (RegistrationForm, LoginForm)
from summer_hack_flask.models import User, AskPost, GivePost, Location
from datetime import datetime
from bson.objectid import ObjectId
from flask_login import login_user, current_user, logout_user, login_required


import json
import requests



with open("./credentials.json") as file:
    credentials = json.load(file)

access_key = credentials["access_key"]

# Landing page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


#Register
@app.route("/register", methods=['GET', 'POST'])
def register():

	if current_user.is_authenticated:
		return redirect(url_for('home'))

	form = RegistrationForm()

	if form.validate_on_submit():

	 	id = ObjectId()
	 	userID = ObjectId()
	 	username =  form.username.data
	 	email = form.email.data
	 	hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
	 	phone =  form.phone.data
	 	firstname = form.firstname.data
	 	lastname = form.lastname.data
	 	created = datetime.utcnow()

	 	# Fetch Ip address
	 	ip_request = requests.get('https://get.geojs.io/v1/ip.json')
	 	my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
	 	geo_request_url = "http://api.ipstack.com/" + my_ip+ "?" + "access_key="+access_key
	 	geo_request = requests.get(geo_request_url)
	 	geo_data = geo_request.json()

	 	# Getting the geo information of the user
	 	country = geo_data['country_name']
	 	state = geo_data['region_name']
	 	city = geo_data['city']
	 	latitude = geo_data['latitude']
	 	longitude = geo_data['longitude']
	 	zipcode = geo_data['zip']


	 	location = Location(country=country, state=state, city=city, latitude=latitude, longitude=longitude, zipcode=zipcode)
	 	user = User(_id=id, userID=userID, username=username, email=email, password=hashed_password, phone=phone, firstName = firstname, lastName = lastname, created=created, location=location)
	 	user.save()
	 	flash('Your account has been created! You are now able to log in', 'success')
	 	return redirect(url_for('login'))

	return render_template('register.html', title='Register', form=form)



#Login
@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))

	form = LoginForm()
	if form.validate_on_submit():
		email = form.email.data
		password = form.password.data
		user = User.objects(email=email).first()
		print(user['password'])
		#print(bcrypt.check_password_hash(user['password'], password))

		if bcrypt.check_password_hash(user['password'], password) == 0:
			flash('Login Unsuccessful. Please check email and password', 'danger')
		else:
			login_user(user, remember=form.remember.data)
			flash('Login Successful', 'success')
			return redirect(url_for('home'))

	return render_template('login.html', form = form)



#Logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

#Offerings
@app.route('/offerings')
@login_required
def offerings():
    return render_template("offerings.html")

@app.route('/post')
def post():
    return render_template("post.html")


@app.route('/filters')
def filters():  
    return 'help'

@app.route('/community')
def community():
    return 'help'