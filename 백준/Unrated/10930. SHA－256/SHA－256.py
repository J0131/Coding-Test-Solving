import hashlib

a = input()
result = hashlib.sha256(a.encode()).hexdigest()
print(result)