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
import telegram
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.utils.helpers import escape_markdown

###################
#####-SETUP-#######
###################

#UNCOMMENT IN PRODUCTION SERVER
#from flask_heroku import Heroku


# create the application object
app = Flask(__name__)
app.config.from_object('_config')

global bot
bot = telegram.Bot(token = "497175063:AAGyWKEuQ39vIEl7E79wLjDVkfcFa5tnyAk")
botName = "In memory of @thegali" #Without @

#UNCOMMENT IN PRODUCTION SERVER
#heroku = Heroku(app)

###################
#####-ROUTING-#####
###################

db = SQLAlchemy(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/gaali', methods=['POST', 'GET'])
def gaali():
	if request.method == 'POST':
		update = telegram.Update.de_json(request.get_json(force=True), bot)
		if not update:
			return("Show me your token")
		elif update.message:
			give(update.message)
		return ("OK!")
	else:
		error = "Invalid"
		return render_template('index.html', error = error)

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


def give(msg):
    text = msg.text

    if text == "/gaalieng" or text == "/gaalieng@Gaalibot":
        bot.sendMessage(chat_id = msg.chat.id, text = getEnglishWord())
        return None
    elif text == "/gaalihindi" or text == "/gaalieng@Gaalibot":
        bot.sendMessage(chat_id = msg.chat.id, text = getHindiWord())
        return None
    elif text == "/help" or text == "/help@gaalibot":
        bot.sendMessage(chat_id = msg.chat.id, text = "In sweet memory of @thegali. If you know where he is, please drag his ass back to telegram.")
        return None
    elif text == "/start":
    	bot.sendMessage(chat_id = msg.chat.id, text = "Blame @BiharEAzam, this is his idea.")


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)