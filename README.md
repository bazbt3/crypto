<img src="crypto_pushover_icon.jpg" width="96" alt="crypto Cryptocurrency alerts.">

The example application sends a Pushover alert and a message to my pnut.io dev channel: with three cryptocurrency values (the equivalent in GBP and the user's holding also in GBP), their movement within the preceding hour, including a message if any exceeds a value hard coded within the application. A graph is created for each currency and saved in the application folder, and added to the Pushover alert message (though not the pnut.io message yet.)

Application is currently tested in Pythonista and at pythonanywhere.com and my web host, and run every hour either as a pythonanywhere 'task' or a cron job at my web host.

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
* pnut.io and Pushover account application and user tokens - read from separate files to give some portability to the code:
 * `pnut_app_token.txt`
 * `pushover_app_token.txt`
 * `pushover_user_token.txt`
* The PNUTpy libraries: `pip install pnutpy`.
* For graphing: `pip install matplotlib`.
* One text file for each of the cryptocurrencies desired, named as `crypto_(currency 3 letter name)_values.txt'. Note: the 'btc' graph is necessary, as the only one sent as a Pushover alert.