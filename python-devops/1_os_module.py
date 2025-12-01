
import os

print("Current directory:", os.getcwd())

if not os.path.exists("logs"):
    os.makedirs("logs")

for f in os.listdir("."):
    print(" ->", f)

token = os.getenv("API_TOKEN")
print("Token:", "Found" if token else "Missing")
