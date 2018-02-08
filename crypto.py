# crypto
# Cryptocurrency alerts
# v0.7.6 for Python 3.5

# Define coins:
# Define coins and alert high limits:
coins = {
	'btc': 12000,
	'eth': 1250,
	'xrp': 2
	}

# Define coin holdings:
holdings = {
	'btc': 0.00484719,
	'eth': 0.07431345,
	'xrp': 35.893
	}

# INITIAL SETUP:

# Graphing:
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# For Pushover alerts:
import http.client, urllib

# For Cryptocurrency and Pushover:
import requests

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

# DEFINE REQUEST FOR CURENCY DATA FROM CRYPTONATOR API:

# get_price function taken unmodified (except for definition of global data) from: https://github.com/jakewmeyer/Crypto
# Uses data from https://www.cryptonator.com/api

# Already done above:
#import requests

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

# GET CURRENCIES, COMPLIME MESSAGE AND GRAPHS:

for coin, alert in coins.items():

	# Open historic values file:
	y = open('crypto_' + coin + '_values.txt', 'r')
	y = y.readlines()

	# Get latest value from cryptonator API:
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

	# Store a maximum of the last 24 data elements for each currency, and create and save graphs:

	# Pop first element from list, append latest value to list:
	if len(y) >= 24:
		y.pop(0)
	y.append(str(value) + '\n')

	# Save the list to file:
	f=open('crypto_' + coin + '_values.txt','w')
	for ele in y:
		f.write(ele)
	f.close()

	# Plot a basic graph:
	fig = plt.figure()
	plt.plot(y)
	plt.ylabel('GBP / ' + coin.upper())

	# Save a .jpg file, overwriting any already there:
	fig.savefig('crypto_' + coin + '_plot.jpg')

# Strip the final, superfluous divider:
pushover_message = pushover_message.rstrip(' | ')

# SEND PUSHOVER MESSAGE:

# From https://pushover.net/faq#library
# Already done above:
#import requests
r = requests.post("https://api.pushover.net/1/messages.json", data = {
  "token": app_token,
  "user": user_token,
  "message": pushover_message
},
files = {
  "attachment": ("image.jpg", open("crypto_btc_plot.jpg", "rb"), "image/jpg")
})

# PNUT.IO message:

# Create message in channel 962, using ONLY the text from pushover_message:
posttext = pushover_message
channelid = 962
postcontent = pnutpy.api.create_message(channelid, data={'text': posttext})
