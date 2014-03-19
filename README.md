tiny-antigate
=============

Tinest (as I can imagine) angigate api wrapper

## Reasons
* [Antigate](https://github.com/gotlium/antigate) wrapper uses [grablib](http://grablib.org/), so it comes with a bit more dependences (like pycurl, lxml, etc.).
* [requests](docs.python-requests.org) is just awesome!
* [Antigate](https://github.com/gotlium/antigate) wants filename of captcha, but in most cases you need to pass 'this' bytes (from requests response, for example), and you defenitly don't want to create files.
* uniform calls

## Requirements
* Python 3
* requests

## Usage
Creating:
```python
import antigate
a = antigate.Antigate(your_key_from_antigate)
```

Sending captcha:
```python
status, captcha_id = a.send(bytes_of_your_captcha)
```
Status can be 'OK' or 'ERROR_*' from [antigate list](http://antigate.com/panel.php?action=api) (added 'ERROR_HTTP' for requests errors). If 'OK' captcha_id really is captcha id, on 'ERROR_HTTP' it is HTTP status code and None in all other cases.

Getting status
```python
status, text = a.status(captcha_id)
```
Status can be 'OK' or 'CAPCHA_NOT_READY' (yeah, ca*pc*ha, it's antigate mistake) or 'ERROR_*' from previous example

Abuse:
```python
status, data = a.abuse(captcha_id)
```

Balance:
```python
balance, data = a.balance()
```
