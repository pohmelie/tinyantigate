tinyantigate
============

Tinest (as I can imagine) antigate/anti-captcha api wrapper. It's just a **subset** of antigate api. It can only:
* send captcha
* check captcha status
* check balance
* abuse

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
* 'ERROR_*', None (from [antigate list](https://anti-captcha.com/apidoc))
* 'ERROR_HTTP', status_code (requests errors)

### Automatic (most common usage)
#####antigate function
```python
from tinyantigate import antigate
status, text = antigate(
    your_key_from_antigate,
    bytes_of_your_captcha,
    timeout=5,                  # \
    count=6,                    #  ) default values (can be omitted)
    host="anti-captcha.com",    # /
)
```
This function is just wrapper around creation Antigate object and calling 'run' function.

### Manual usage

##### Creating:
```python
import tinyantigate
a = tinyantigate.Antigate(your_key_from_antigate, host="anti-captcha.com")
```

##### Sending captcha:
```python
status, captcha_id = a.send(bytes_of_your_captcha)
```
Return values:
* 'OK', captcha_id

##### Getting status:
```python
status, text = a.status(captcha_id)
```
Return values:
* 'OK', captcha_text
* 'CAPCHA_NOT_READY', None (yeah, CA**PC**HA_NOT_READY, it's antigate funny mistake)

##### Abuse:
```python
status, data = a.abuse(captcha_id)
```
Return values:
* "", None

##### Balance:
```python
balance, data = a.balance()
```
Return values:
* balance, None

`balance` as string

##### Run:
```python
status, text = a.run(bytes_of_your_captcha, timeout=5, count=6)
```
Mix of 'send' and 'status' functions. Timeout is the delay between checks of captcha status. Count is number of checks.

Return values:

Same as for 'send' and 'status' functions.
