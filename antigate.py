import requests
import time


class Antigate():

    def __init__(self, key, host="antigate.com"):

        self.key = key
        self.host = host


    def build_url(self, suburl):

        return str.format("http://{}/{}", self.host, suburl)


    def get_action_url(self, **kwargs):

        kwargs["key"] = self.key
        actions = map(lambda item: str.format("{}={}", *item), kwargs.items())
        return self.build_url("res.php?") + str.join("&", actions)


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


    def action(self, **kwargs):

        return self.parse_answer(
            requests.get(
                self.get_action_url(**kwargs)
            )
        )


    def status(self, cid):

        return self.action(action="get", id=cid)


    def abuse(self, cid):

        return self.action(action="reportbad", id=cid)


    def balance(self):

        return self.action(action="getbalance")


    def run(self, captcha, timeout=5, count=6):  # 30 seconds timeout (5s for 6 times)

        status, captcha_id = self.send(captcha)
        if status != "OK":

            return status, captcha_id

        for _ in range(count):

            time.sleep(timeout)
            status, text = self.status(captcha_id)
            if status == "OK" or status != "CAPCHA_NOT_READY":

                return status, text

        return "CAPCHA_NOT_READY", None


def antigate(key, captcha, timeout=5, count=6, host="antigate.com", ):

    a = Antigate(key, host)
    return a.run(captcha, timeout, count)
