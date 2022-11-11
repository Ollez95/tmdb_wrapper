from abc import ABC, abstractmethod
import requests
from requests import Response


class Request(ABC):
    '''
    Abstract Class to get different requests
    '''
    @abstractmethod
    def request(
        self,
        url,
        params = None,
        data = None,
        headers = None,
        timeout = None) -> Response:
        pass


class GetRequest(Request):
    '''
    Class with GET request
    '''
    def request(self, url, params = None, data = None, headers = None, timeout = 5) -> Response:
        return requests.get(url = url, params = params, headers = headers, timeout= timeout)


class PostRequest(Request):
    '''
    Class with POST request
    '''
    def request(self, url, params = None, data = None, headers = None, timeout = 5) -> Response:
        return requests.post(
            url = url,
            params = params,
            data = data,
            headers = headers,
            timeout= timeout)


class DeleteRequest(Request):
    '''
    Class with DELETE request
    '''
    def request(self, url, params = None, data = None, headers = None, timeout = 5) -> Response:
        return requests.delete(
            url = url,
            params=params,
            data=data,
            headers = headers,
            timeout= timeout)


class PutRequest(Request):
    '''
    Class with PUT request
    '''
    def request(self, url, params = None, data = None, headers = None, timeout = 5) -> Response:
        return requests.put(
            url = url,
            params = params,
            headers = headers,
            timeout= timeout)