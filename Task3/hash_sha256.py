import hashlib

with open("data.txt", "rb") as f:
    data = f.read()

hash_output = hashlib.sha256(data).hexdigest()
print("SHA-256:", hash_output)
