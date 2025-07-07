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

    def cancelOrder(self, params):
        return self._request_with_params(POST, '/api/v3/trade/cancel-order', params)
    
    def getOrder(self, params):
        return self._request_with_params(GET, '/api/v3/trade/order-info', params)
    
    def closePositions(self, params):
        return self._request_with_params(POST, '/api/v3/trade/close-positions', params)

   