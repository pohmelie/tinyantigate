tiny-antigate
=============

Tinest (as I can imagine) angigate api wrapper

# Reasons
* [Antigate](https://github.com/gotlium/antigate) wrapper uses [grablib](http://grablib.org/), so it comes with a bit more dependences (like pycurl, lxml, etc.).
* [requests](docs.python-requests.org) is just awesome!
* [Antigate](https://github.com/gotlium/antigate) wants filename of captcha, but in most cases you need to pass 'that' bytes (from requests response, for example), and you defenitly don't want to create files.

# Requirements
* Python 3
* requests

# Usage
Creating
```python
import antigate
a = antigate.Antigate(your_key_from_antigate)
```

Sending captcha
```python
status, captcha_id = a.send(bytes_of_your_captcha)
```
Status can be 'OK' or 'ERROR_*' from [antigate list](http://antigate.com/panel.php?action=api) (added 'ERROR_HTTP' for requests errors). If 'OK' captcha_id really is captcha id, on 'ERROR_HTTP' it is HTTP status code and None in all other cases.
