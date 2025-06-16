#!/usr/bin/python
from bitget.client import Client
from bitget.consts import GET, POST

class AccountApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def assets(self, params):
        return self._request_with_params(GET, '/api/v3/account/assets', params)
    
    def settings(self, params):
        return self._request_with_params(GET, '/api/v3/account/settings', params) 
    
    def setLeverage(self, params):
        return self._request_with_params(POST, '/api/v3/account/set-leverage', params)
    
    def setHoldMode(self, params):
        return self._request_with_params(POST, '/api/v3/account/set-hold-mode', params)
