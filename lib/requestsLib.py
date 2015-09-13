__author__ = 'rakesh.varma'
import requests

class requestsLib:

    def __init__(self, url, headers, payload):
        self.url = url
        self.payload = payload
        self.headers = headers

    def response(self):
        return requests.post(self.url, headers = self.headers, data = self.payload)

