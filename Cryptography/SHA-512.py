import hashlib

data=input("Enter Your data :- ")

result=hashlib.sha512(data.encode())

print("The Hexadesimal hash value of SHA512:-")

print(result.hexdigest())
