import requests
import time


__version__ = "0.1.0"

DEFAULT_HOST = "anti-captcha.com"


class Antigate():

    def __init__(self, key, host=DEFAULT_HOST):

        self.key = key
        self.host = host

    def build_url(self, suburl):

        return str.format("http://{}/{}", self.host, suburl)

    def parse_answer(self, r):

        if r.status_code != requests.codes.ok:

            return "ERROR_HTTP", r.status_code

        elif str.startswith(r.text, "OK|"):

            return str.split(r.text, "|")

        else:

            return r.text, None

    def send(self, captcha):

        return self.parse_answer(
            requests.post(
                self.build_url("in.php"),
                data={
                    "key": self.key,
                },
                files={
                    "file": captcha,
                },
            )
        )

    def action(self, **payload):

        payload["key"] = self.key
        return self.parse_answer(
            requests.get(
                self.build_url("res.php"),
                params=payload
            )
        )

    def status(self, cid):

        return self.action(action="get", id=cid)

    def abuse(self, cid):

        return self.action(action="reportbad", id=cid)

    def balance(self):

        return self.action(action="getbalance")

    def run(self, captcha, timeout=5, count=6):

        status, captcha_id = self.send(captcha)
        if status != "OK":

            return status, captcha_id

        for _ in range(max(1, count)):

            time.sleep(timeout)
            status, text = self.status(captcha_id)
            if status != "CAPCHA_NOT_READY":

                break

        return status, text


def antigate(key, captcha, timeout=5, count=6, host=DEFAULT_HOST):

    return Antigate(key, host).run(captcha, timeout, count)
