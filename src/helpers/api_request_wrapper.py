# helpers/api_request_wrapper.py

import requests
from src.constants.api_constants import BASE_URL

def post_request(path, headers=None, payload=None):
    """Send a POST request."""
    url = BASE_URL + path
    response = requests.post(url=url, headers=headers, json=payload)
    return response



def put_request(path, headers=None, payload=None):
    """Send a PUT request."""
    url = BASE_URL + path
    response = requests.put(url=url, headers=headers, json=payload)
    return response

def delete_request(path, headers=None):
    """Send a DELETE request."""
    url = BASE_URL + path
    response = requests.delete(url=url, headers=headers)
    return response
