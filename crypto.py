# crypto
# Cryptocurrency alerts
# v0.6 for Python 3.5

# Define coins and alert high limits:
coins = {
	'btc': 12000,
	'eth': 800,
	'xrp': 2
	}

# Define coin holdings:
holdings = {
	'btc': 0.00484719,
	'eth': 0.07431345,
	'xrp': 35.893
	}


# For Pushover alerts:
import http.client, urllib

# Import @33MHz and @thrrgilag's library for interacting with pnut.io:
import pnutpy

# Define global data variable (until get_price is changed to return 'change')
global data

# Setup Pushover authorisation:
pushover_message = ''
# Read app token from file:
tokenfile = open('pushover_app_token.txt', "r")
app_token = tokenfile.read()
app_token = app_token.strip()
# Read user token from file:
tokenfile = open('pushover_user_token.txt', "r")
user_token = tokenfile.read()
user_token = user_token.strip()

# Setup pnut.io authorisation:
tokenfile = open("pnut_app_token.txt", "r")
token = tokenfile.read()
token = token.strip()
pnutpy.api.add_authorization_token(token)


# get_price function taken unmodified from: https://github.com/jakewmeyer/Crypto
# Uses data from https://www.cryptonator.com/api

import requests

def get_price(coin, base_currency):
	"""Returns current price of given coin in the respective currency"""
	global data
	try:
		url = "https://api.cryptonator.com/api/ticker/{}-{}".format(
			coin, base_currency)
		request = requests.get(url)
		if request.status_code == 200:
			data = request.json()
	except requests.exceptions.RequestException:
		return "Coin not found"
	if not data['success']:
		raise Exception("Coin not found")
	else:
		return data['ticker']['price']

# Extract GBP values for BTC, ETH and XRP, and alert on values exceeding preset limits:
for coin, alert in coins.items():
	value = get_price(coin,'gbp')
	value = round(float(value),2)
	change = float(data['ticker']['change'])
	exceeded = ''
	if value >= alert:
		exceeded = "*limit! "
	indicator = ''
	if change < 0:
		indicator = '-'
	elif change > 0:
		indicator = '+'
	holding = holdings[coin]
	real_money = round(float(value * holding),2)
	message = exceeded + coin.upper() + ': £' + str(value) + indicator + ' £' + str(real_money)
	pushover_message += message + ' | '

# Strip the final, superfluous divider
pushover_message = pushover_message.rstrip(' | ')


# PUSHOVER MESSAGE:

# From https://pushover.net/faq#library
conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": app_token,
    "user": user_token,
    "message": pushover_message,
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()


# PNUT.IO message:

# Create message in channel 962, using the text from pushover_message:
posttext = pushover_message
channelid = 962
postcontent = pnutpy.api.create_message(channelid, data={'text': posttext})
