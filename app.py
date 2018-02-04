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

if __name__ == '__main__':
	app.run(debug=True)