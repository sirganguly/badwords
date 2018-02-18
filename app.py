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

#init telegram bot
global bot
bot = telegram.Bot(token = "497175063:AAGyWKEuQ39vIEl7E79wLjDVkfcFa5tnyAk")
#incase you are wondering, the above secret has since been revoked and was commited by mistake. Use your own.
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
		#store the incoming telegram json object
		update = telegram.Update.de_json(request.get_json(force=True), bot)
		#ask for a correct token
		if not update:
			return("Show me your token")
		elif update.message:
			#call function to take the appropriate action
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


'''
	The following actions(fuction calls) will have to be updated once we use start using postgres or other databses.
'''
def give(msg):
	#store the text element from the passed in object
    text = msg.text
    if text == "/gaalieng" or text == "/gaalieng@Gaalibot":
        bot.sendMessage(chat_id = msg.chat.id, text = getEnglishWord())
        return None
    #get Hindi gaali
    elif text == "/gaalihindi" or text == "/gaalihindi@Gaalibot":
        bot.sendMessage(chat_id = msg.chat.id, text = getHindiWord())
        return None
    #static actions
    elif text == "/help" or text == "/help@gaalibot":
        bot.sendMessage(chat_id = msg.chat.id, text = "In sweet memory of @thegali. If you know where he is, please drag his ass back to telegram.")
        return None
    elif text == "/start":
    	bot.sendMessage(chat_id = msg.chat.id, text = "Blame @BiharEAzam, this is his idea. Use '/gaalieng' For English and '/gaalihindi' for Hindi.")


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
