## crypto

### Rough cryptocurrency alerts
Sends a Pushover alert every hour with three cryptocurrency values, their movement within the preceding hour, and an additional message if any exceeds a value hard coded within the application.

### The entire `get_price` function taken from:
https://github.com/jakewmeyer/Crypto - which uses the basic data from https://www.cryptonator.com/api

#### Example hardcoded alert high limits:
```
 btc_alert = 12000
 eth_alert = 1250
 xrp_alert = 2
```
