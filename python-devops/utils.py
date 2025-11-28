import requests, logging

def call_api(url):
    logging.info(f"Calling API: {url}")
    return requests.get(url).json()

def read_file(path):
    with open(path) as f:
        return f.read()
