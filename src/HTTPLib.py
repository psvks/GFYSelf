import requests
from requests import Response


class HttpClient:
    """
    A simple HTTP client that provides common HTTP methods.
    """

    def send_request(self, method: str, endpoint: str) -> Response:
        """
        Sends an HTTP request to the specified endpoint using the specified method.
        """
        method = method.lower()
        methods = {
            'get': requests.get,
            'post': requests.post,
            'put': requests.put,
            'delete': requests.delete,
            'options': requests.options,
            'head': requests.head,
            'patch': requests.patch
        }
        if method in methods:
            return methods[method](endpoint)
        else:
            raise ValueError(f"Invalid HTTP method: {method}")
