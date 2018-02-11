# -*- encoding: utf-8 -*-

'''
This file will contain:
	- API routes for the badwords app
	- serve html
'''

###################
#####-IMPORTS-#####
###################

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session, jsonify, session, send_from_directory
from werkzeug import secure_filename
import os
import random
from randomGenerator import getHindiWord, getEnglishWord
from datetime import datetime

###################
#####-SETUP-#######
###################

#UNCOMMENT IN PRODUCTION SERVER
#from flask_heroku import Heroku


# create the application object
app = Flask(__name__)
app.config.from_object('_config')

#UNCOMMENT IN PRODUCTION SERVER
#heroku = Heroku(app)

###################
#####-ROUTING-#####
###################

db = SQLAlchemy(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/randHindi', methods=['GET'])
def randHindi():
	if request.method == 'GET':
		hindi = getHindiWord()
		return render_template('index.html', hindi = hindi)
	else:
		error = "Invalid"
		return render_template('index.html', error = error)
		
@app.route('/randEnglish', methods=['GET'])
def randEnglish():
	if request.method == 'GET':
		english = getEnglishWord()
		return render_template('index.html', english = english)
	else:
		error = "Invalid"
		return render_template('index.html', error = error)
		
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)