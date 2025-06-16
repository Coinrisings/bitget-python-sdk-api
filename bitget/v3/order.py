#!/usr/bin/python
from bitget.client import Client
from bitget.consts import GET, POST


class OrderApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def placeOrder(self, params):
        return self._request_with_params(POST, '/api/v3/trade/place-order', params)

    def modifyOrder(self, params):
        return self._request_with_params(POST, '/api/v3/trade/modify-order', params)

    def CancelOrder(self, params):
        return self._request_with_params(POST, '/api/v3/trade/cancel-order', params)

   