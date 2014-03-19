import requests


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
