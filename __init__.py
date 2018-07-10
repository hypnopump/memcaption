#-*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import session

# -*- coding: iso-8859-15 -
from flask_cors import CORS, cross_origin
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask.ext.session import Session
import os
import json
import hashlib


app = Flask(__name__)
app.config.from_pyfile('utils/config.py')
app.secret_key = "dafuq?lolasso"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from utils import models
db.create_all()

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def web():
	data = []
	return render_template('index.html', data=data)

@app.route('/demo/')
def demo():
	return render_template('safe_index.html')

@app.route('/post<id>/')
def post(id):
	return render_template('post.html')

@app.route('/leaderboard/')
def leader():
	return render_template('leader.html')

@app.route('/signup/')
def signup():
	return render_template('signup.html', mess=None)

@app.route('/login/')
def login():
	return render_template('login.html')

@app.route('/logger/', methods = ['GET', 'POST'])
def logger():
	email = request.form['email']
	password = hashlib.sha256(bytearray(request.form['password'], "utf-8")).hexdigest()
	if True: # if user_in_db:
		# username = check_db_for_username
		# user_id = check_db_for_id
		session["username"] = "eric_alcaide" # username
		session["email"] = email
		session["id"] = 1 # user_id
	return redirect(url_for('web'))

@app.route('/logout/')
def logout():
	# remove the username, id from the session if it is there
	session.pop('username', None)
	session.pop('id', None)
	session.pop('email', None)
	return redirect(url_for('web'))

@app.route('/new_user/', methods = ['GET', 'POST'])
def new_user():
	username = request.form['username']
	email = request.form['email']
	password = hashlib.sha256(bytearray(request.form['password'], "utf-8")).hexdigest()
	re_password = hashlib.sha256(bytearray(request.form['re_password'], "utf-8")).hexdigest()

	if password != re_password:
		return render_template('signup.html', mess="Passwords don't match")

	return "Data received "+username+" / "+email+" / "+password+" / "+re_password

@app.route('/testing/')
def testing():
	sols = []
	q = models.Reg.query.all()
	for line in q:
		if query in line.name.split(" "):
			sols.append({"name": str(line.name),"link": str(line.hash)})
	return sols

if __name__ == '__main__':
	# # Deploying
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
	# Debugging
	# app.run(debug=True, host='0.0.0.0')
