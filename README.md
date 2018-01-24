<img src="crypto_pushover_icon.jpg" width="96" alt="crypto Cryptocurrency alerts.">

Sends a Pushover alert with three cryptocurrency values (the equivalent in GBP and the user's holding also in GBP), their movement within the preceding hour, including a message if any exceeds a value hard coded within the application.

Application is currently hosted at pythonanywhere.com and run as a 'task' every hour.

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

### Prerequisites:
* Pushover account application and user tokens - read from separate files to give some portability to the code:
 * `pushover_app_token.txt`
 * `pushover_user_token.txt`