from pyDes import *

pt=input("Enter Your Data :-")

key=des("DESCRYPT",ECB,"\0\0\0\0\0\0\0\0",padmode=PAD_PKCS5)

print("encrypted message is")

ct=key.encrypt(pt)
print(ct)

print("decrypted message is")
pt=key.decrypt(ct)
print(pt)


