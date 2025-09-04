alpha="abcdefghijklmnopqrstuvwxyz"

text=input("Enter Your Data:-")
key=int(input("Enter Your Key :-"))

size=len(text)
ct=""

for i in range(size):
    char=text[i]
    index=alpha.find(char)
    ni=(index+key)%26
    ct=ct+alpha[ni]

print(ct)

