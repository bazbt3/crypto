## Changelog
(most recent first)

### v0.76 2018-02-08:
* Changed matplotlib import again, adding `matplotlib.use("Agg")` to sidestep `tkinter` issue. (Unsuccessfully tried @jws' suggestion and now following identical fix from pythonanywhere!)

### v0.7.5 2018-02-04:
* Reverted back to jpg; I'm not certain I got the image parameters correct but my pdf won't render in the Pushover iOS app.

### v0.7.4 2018-02-04:
* Changed filetype to pdf (worth a try; thanks @jws. If it fails I'll try Pillow/PIL.)

### v0.7.3 2018-02-03:
* Minor code comment and graph tweaks.

### v0.7.2 2018-02-03:
* Manual code revert. Failure to create alerts at pythonanywhere, malformed vertical axis labels at my web host.

### v0.7.1 2018-02-03:
* Attempting to fix a dependency on Python `tk` module, which doesn't appear to be installed at my web host. Help from here: https://github.com/matplotlib/matplotlib/issues/9017

### v0.7 2018-02-03:
* A graph is built for each of the cryptocurrencies and saved in the same folder as the application. In the example application, the BTC graph is also sent in the Pushover alert (not enabled for the pnut.io message yet.)

### v0.6.1 2018-01-30:
* Updated ETH limit value.

### v0.6 2018-01-26:
* Added: Message also sent to my pnut.io dev channel.

### v0.5.1 2018-01-24:
* Reinstated GBP per coin values.
* Added Pushover application icon.

### v0.5 2018-01-23:
* Values converted to real-world holdings (cryptocurrency holdings hardcoded.)
* Pushover app and user tokens removed from script to separate files.

### v0.4 2018-01-22:
* Coins examined in loop rather than one block of code for each.

### v0.3 2018-01-21:
* Hourly +/- change added.
* First GitHub commit.

### v0.2:
* High limit alert added (hardcoded in script.)

### v0.1:
* Pushover.net service alert message added.

### v0.0:
* Values printed only to screen.
