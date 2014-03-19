tiny-antigate
=============

Tinest (as I can imagine) antigate api wrapper

## Reasons
* [Antigate](https://github.com/gotlium/antigate) wrapper uses [grablib](http://grablib.org/), so it comes with a bit more dependences (like pycurl, lxml, etc.).
* [requests](docs.python-requests.org) is just awesome!
* [Antigate](https://github.com/gotlium/antigate) wants filename of captcha, but in most cases you need to pass 'this' bytes (from requests response, for example), and you defenitly don't want to create files.
* uniform calls

## Requirements
* Python 3
* requests

## Usage
All methods, can return errors:
* 'ERROR_*', None (from [antigate list](http://antigate.com/panel.php?action=api))
* 'ERROR_HTTP', status_code (requests errors)

### Automatic
```python
import antigate
status, text = antigate.antigate(
    your_key_from_antigate,
    bytes_of_your_captcha,
    timeout=5,
    count=6,
    host="antigate.com",
)
```
Timeout is the delay between checks of captcha status. Count is number of checks.

### Manual usage
Creating:
```python
import antigate
a = antigate.Antigate(your_key_from_antigate)
```

Sending captcha:
```python
status, captcha_id = a.send(bytes_of_your_captcha)
```
Return values:
* 'OK', captcha_id

Getting status:
```python
status, text = a.status(captcha_id)
```
Return values:
* 'OK', captcha_text
* 'CAPCHA_NOT_READY', None (yeah, CA**PC**HA_NOT_READY, it's antigate funny mistake)

Abuse:
```python
status, data = a.abuse(captcha_id)
```
Return values:
* "", None

Balance:
```python
balance, data = a.balance()
```
Return values:
* balance, None
