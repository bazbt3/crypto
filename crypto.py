# crypto
# Cryptocurrency alerts
# v0.4 for Python 3.5

# Define coins and alert high limits:
coins = {
	'btc': 12000,
	'eth': 800,
	'xrp': 2
	}

# Define global data variable (until get_price is changed to return 'change')
global data

# For Pushover alert:
import http.client, urllib
pushover_message = ''

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
	# Extract GBP values for BTC, ETH and XRP, and alert on values exceeding preset limits:
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
	message = exceeded + coin + ': £' + str(value) + indicator
	pushover_message += message + ' | '

pushover_message = pushover_message.rstrip(' | ')
	
# Send message to Pushover:
conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": "[REDACTED]",
    "user": "[REDACTED]",
    "message": pushover_message,
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
