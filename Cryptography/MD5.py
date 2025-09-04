import hashlib

plaintext=input("Enter Your Data :-")

result=hashlib.md5(b'&plaintext')



print(result.digest())
