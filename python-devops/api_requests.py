import requests

def api_get(url):
    return requests.get(url).json()

def api_post(url, payload):
    return requests.post(url, json=payload).json()
