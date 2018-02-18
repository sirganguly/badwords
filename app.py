# -*- encoding: utf-8 -*-

'''
This file will contain:
	- API routes for the badwords app
	- serve html
'''

###################
#####-IMPORTS-#####
###################

from flask import Flask, render_template, request
from urllib import parse as urlparse
import psycopg2 as postgres
import randomGenerator
import telegram
import os


#Flask configuration
# create the application object
app = Flask(__name__)
app.config.from_object('_config')


#Telegram bot configuration
global bot
bot = telegram.Bot(token = "YOUR TELEGRAM TOKEN GOES HERE")
botName = "In memory of @thegali"


#Postgresql configuration
'''
	Run the following command after having logged into heroku on your terminal to copy the current local database to heroku, that is assuming that you have a populated database.

	Add the addon
	heroku addons:create heroku-postgresql:hobby-dev

	Push local database to heroku
	heroku pg:push your_database_name DATABASE_URL --app your_appname


	For more features and settings visit: https://devcenter.heroku.com/articles/heroku-postgresql

'''

'''

	Following are to be commented during production push.

	conn = postgres.connect(dbname = "gaali", user = "postgres", host = "localhost")

'''

'''
	Current database contains two tables: Hindi and English
'''

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = postgres.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

cur = conn.cursor()

#--------------------------------------Flask Starts--------------------------------------#

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
		hindi = randomGenerator.FetchBadWord(cur)
		return render_template('index.html', hindi = hindi.hindi())
	else:
		error = "Invalid"
		return render_template('index.html', error = error)

@app.route('/randEnglish', methods=['GET'])
def randEnglish():
	if request.method == 'GET':
		english = randomGenerator.FetchBadWord(cur)
		return render_template('index.html', english = english.english())
	else:
		error = "Invalid"
		return render_template('index.html', error = error)

#-------------------------------------- Flask Ends --------------------------------------#

def give(msg):
    text = msg.text

    if text == "/gaalieng" or text == "/gaalieng@Gaalibot":
    	english = randomGenerator.FetchBadWord(cur)
    	bot.sendMessage(chat_id = msg.chat.id, text = english.english())
    	return None
    elif text == "/gaalihindi" or text == "/gaalihindi@Gaalibot":
    	hindi = randomGenerator.FetchBadWord(cur)
    	bot.sendMessage(chat_id = msg.chat.id, text = hindi.hindi())
    	return None
    elif text == "/help" or text == "/help@gaalibot":
        bot.sendMessage(chat_id = msg.chat.id, text = "In sweet memory of @thegali. If you know where he is, please drag his ass back to telegram.")
        return None
    elif text == "/start":
    	bot.sendMessage(chat_id = msg.chat.id, text = "Blame @BiharEAzam, this is his idea.")


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)