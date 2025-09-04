import onetimepad




cipher=onetimepad.encrypt('abc','random')
print("Cipher text is:-",cipher)


print(" ----decryption----")

plaintext=onetimepad.decrypt(cipher,'random')

print("plain text is :-",plaintext)
