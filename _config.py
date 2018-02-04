# -*- encoding: utf-8 -*-

'''
This file will contain:
	- configuration information for the Flask server

'''

import os

#grab folder where script lives
basedir = os.path.abspath(os.path.dirname(__file__))
JSON_AS_ASCII = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

# This is the path to the upload directory
UPLOAD_FOLDER = 'uploads/'

DATABASE = '<db_name>.db'
WTF_CSRF_ENABLED = True

#to be generated when we deploy to heroku but NOT to be shared on github public repo
SECRET_KEY = """<your-secret-key-goes-here>"""

#############################################
#COMMENT OUT BELOW LINES IN PRODUCTION SERVER

DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

#############################################