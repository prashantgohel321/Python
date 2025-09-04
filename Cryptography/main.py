from pyDes import *

PT=input("Enter Your Data :- ")

key  =des("DESCRYPT",ECB,"\0\0\0\0\0\0\0\0",padmode=PAD_PKCS5)

ct=key.encrypt(PT)
PT=key.decrypt(ct)

print("Enrypted :",ct)
print("Decrypted :",PT)

