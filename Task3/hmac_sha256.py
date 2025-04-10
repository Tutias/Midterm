import hmac
import hashlib

key = b"secretkey123"

with open("data.txt", "rb") as f:
    data = f.read()

hmac_output = hmac.new(key, data, hashlib.sha256).hexdigest()
print("HMAC-SHA256:", hmac_output)
