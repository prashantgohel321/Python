import hashlib

pt=input("Enter Your Data :-")

result=hashlib.sha1(pt.encode())

print(result.hexdigest())

print(result)
