## crypto

### Rough cryptocurrency alerts
Sends a Pushover alert every hour\* with three cryptocurrency values, their movement within the preceding hour, with a message if any exceeds a value hard coded within the application.

\*Application is currently hosted at pythonanywhere.com and run as a 'task' every hour.

### The entire `get_price` function taken from:
https://github.com/jakewmeyer/Crypto - which uses the basic data from https://www.cryptonator.com/api

#### Example hardcoded alert high limits:
```
coins = {
	'btc': 12000,
	'eth': 800,
	'xrp': 2
	}
```
