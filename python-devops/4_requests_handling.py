
import requests
import os

resp=requests.get("https://httpbin.org/get")
print(resp.json())

payload={"name":"manoj"}
resp=requests.post("https://httpbin.org/post", json=payload)
print(resp.json())
