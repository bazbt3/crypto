# crypto
# Cryptocurrency alerts
# v0.5 for Python 3.5

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

# Define global data variable (until get_price is changed to return 'change')
global data

# For Pushover alerts:
import http.client, urllib
pushover_message = ''
# Read app token from file:
tokenfile = open('pushover_app_token.txt', "r")
app_token = tokenfile.read()
app_token = app_token.strip()
# Read user token from file:
tokenfile = open('pushover_user_token.txt', "r")
user_token = tokenfile.read()
user_token = user_token.strip()

# get_price function taken from: https://github.com/jakewmeyer/Crypto
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
	message = exceeded + coin + ': £' + str(real_money) + indicator
	pushover_message += message + ' | '

pushover_message = pushover_message.rstrip(' | ')
	
# Send message to Pushover:
conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": app_token,
    "user": user_token,
    "message": pushover_message,
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
