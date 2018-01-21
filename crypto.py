# crypto
# Cryptocurrency alerts
# v0.3 2017-01-20

# Define alert high limits:
btc_alert = 12000
eth_alert = 1250
xrp_alert = 2

# Define global data variable (until get_price is changed to return 'change')
global data

# For Pushover alert:
import http.client, urllib

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
btc_value = get_price('btc','gbp')
btc_value = round(float(btc_value),2)
btc_change = float(data['ticker']['change'])
btc_indicator = ''
if btc_change < 0:
	btc_indicator = '-'
elif btc_change > 0:
	btc_indicator = '+'
btc_message = 'BTC: £' + str(btc_value) + btc_indicator

eth_value = get_price('eth','gbp')
eth_value = round(float(eth_value),2)
eth_change = float(data['ticker']['change'])
eth_indicator = ''
if eth_change < 0:
	eth_indicator = '-'
elif eth_change > 0:
	eth_indicator = '+'
eth_message = 'ETH: £' + str(eth_value) + eth_indicator

xrp_value = get_price('xrp','gbp')
xrp_value = round(float(xrp_value),2)
xrp_change = float(data['ticker']['change'])
xrp_indicator = ''
if xrp_change < 0:
	xrp_indicator = '-'
elif xrp_change > 0:
	xrp_indicator = '+'
xrp_message = 'XRP: £' + str(xrp_value) + xrp_indicator

# Check if each coin value has been exceeded, if so compose alert message
alert_message = ''
if btc_value >= btc_alert:
	alert_message += '*BTC value exceeded:*\n'
if eth_value >= eth_alert:
	alert_message += '*ETH value exceeded:*\n'
if xrp_value >= xrp_alert:
	alert_message += '*XRP value exceeded:*\n'

# Compile message and send to Pushover
pushover_message = alert_message + btc_message + ' | ' + eth_message + ' | ' + xrp_message

conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": "[REDACTED]",
    "user": "[REDACTED]",
    "message": pushover_message,
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()