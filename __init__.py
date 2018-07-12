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
from flask_session import Session
import os
import json
import hashlib


app = Flask(__name__)
app.config.from_pyfile('utils/config.py')
app.secret_key = "dafuq?lolasso"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from utils import models
# db.create_all()

# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def web():
	data = []
	return render_template('index.html', data=data)

@app.route('/demo/')
def demo():
	return render_template('safe_index.html')

@app.route('/post<id>/')
def post(id):
	image = models.Img.query.filter_by(id=id).first()
	# retrieve comments and sort by popularity
	comments = models.Comment.query.filter_by(img_id=id)
	comments = [x for x in sorted(comments, key=lambda x: x.score, reverse=True)]
	return render_template('post.html', image=image, comments=comments)

@app.route('/add_comment/', methods=['POST'])
def add_comment():
	username = session["username"]
	text = request.form['text']
	img_id = request.form['img_id']
	score = 0
	voters = ""

	comment = models.Comment(username, text, img_id, score, voters)
	db.session.add(comment)
	db.session.commit()
	return redirect('/post'+img_id+'/')

@app.route('/voter<id>/')
def upvote(id):
	#Check if session is active
	if session.get("username"):
		comment = models.Comment.query.filter_by(id=id).first()
		if session["username"] not in comment.voters.split(""):
			comment.score += 1
			comment.voters += session["username"]+" "
			db.session.commit()

		return redirect('/post'+id+'/')
	# Don't allow voting if not logged in
	else:
		return redirect(url_for("login"))

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
	# Check if user is registered in db
	in_db = models.User.query.filter_by(email=email, password=password).first()
	if in_db: # if user_in_db: update session values
		username = in_db.username
		user_id = in_db.id
		session["username"] = username
		session["email"] = email
		session["id"] = user_id
		return redirect(url_for('web'))
	else:
		return render_template('login.html', mess="Email or password are incorrect")

@app.route('/logout/')
def logout():
	# remove the username, id from the session if it is there
	if session.get("username"):
		session.pop('username', None)
		session.pop('id', None)
		session.pop('email', None)
	return redirect(url_for('web'))

@app.route('/new_user/', methods = ['GET', 'POST'])
def new_user():
	# if not all fields complete, don't allow sign up
	if request.form['username'] == "" or request.form['email'] == "" or request.form['password'] == "":
		return render_template('signup.html', mess="Fill all the items please")

	username = request.form['username']
	email = request.form['email']
	password = hashlib.sha256(bytearray(request.form['password'], "utf-8")).hexdigest()
	re_password = hashlib.sha256(bytearray(request.form['re_password'], "utf-8")).hexdigest()

	# Check if username/email is already in db
	name_in_db = models.User.query.filter_by(username=username).first()
	email_in_db = models.User.query.filter_by(email=email).first()
	if name_in_db or email: # if user_in_db: update session values
		return render_template('signup.html', mess="Email or username are already registered")
	# Check if passwords don't match
	elif password != re_password:
		return render_template('signup.html', mess="Passwords don't match")
	# If everything is correct, add user to DB and redirect to login
	else:
		user = models.User(username, email, password)
		db.session.add(user)
		db.session.commit()
		return render_template('login.html', mess="Signed up successfully")

@app.route('/testing/')
def testing():
	# Check users working correctly
	sols = []
	q = models.User.query.all()
	db.session.commit()
	for line in q:
		sols.append({"id": str(line.id),
					"name": str(line.username),
					"email": str(line.email), 
					"password": str(line.password)})
	# Check comments working correctly 
	comms = []
	q = models.Comment.query.all()
	db.session.commit()
	for line in q:
		comms.append({"id": str(line.id),
					"name": str(line.username),
					"text": str(line.text), 
					"img_id": str(line.img_id),
					"score": str(line.score)})
	# Check images working correctly 
	imgs = []
	q = models.Img.query.all()
	db.session.commit()
	for line in q:
		imgs.append({"id": str(line.id),
					"name": str(line.name),
					"source_name": str(line.source_name), 
					"source_link": "https://"+str(line.source_link)})
	return str(sols)+"\n \n"+str(comms)+"\n \n"+str(imgs)

if __name__ == '__main__':
	# # Deploying
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
	# Debugging
	# app.run(debug=True, host='0.0.0.0')
