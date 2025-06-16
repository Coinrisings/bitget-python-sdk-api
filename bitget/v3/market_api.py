#!/usr/bin/python
from bitget.client import Client
from bitget.consts import GET


class MarketApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def instruments(self, params):
        return self._request_with_params(GET, '/api/v3/market/instruments', params)
    
    def tickers(self, params):
        return self._request_with_params(GET, '/api/v3/market/tickers', params)

    def orderbook(self, params):
        return self._request_with_params(GET, '/api/v3/market/orderbook', params)   
    
    def fills(self, params):
        return self._request_with_params(GET, '/api/v3/market/fills', params)

    def candles(self, params):
        return self._request_with_params(GET, '/api/v3/market/candles', params)   
   
   
   
   
    