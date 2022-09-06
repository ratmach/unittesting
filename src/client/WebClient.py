import requests


class WebClient:
    def make_get_request(self, *args, **kwargs):
        raise Exception("You're not allowed to make http requests from the integration environment")

    def make_post_request(self, *args, **kwargs):
        raise Exception("You're ")
