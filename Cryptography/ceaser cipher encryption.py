#ceaser cipher encryption

alpha="abcdefghijklmnopqrstuvwxyz"

plaintext=input("Enter Youe Data :-")
key=int(input("Enter Your Key :-"))

size=len(plaintext)
ciphertext=""

for i in range(size):
    char=plaintext[i]
    index=alpha.find(char)
    newindex=(index+key)%26

    ciphertext=ciphertext + alpha[newindex]
print(ciphertext)

