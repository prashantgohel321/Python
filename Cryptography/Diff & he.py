#difie Helman 

# Variables Used
sharedPrime = 11  # n
sharedBase = 7  # g

aliceSecret = 3  # x
bobSecret = 6  # y

# Begin
print("Publicly Shared Variables:")
print("    Publicly Shared Prime: ", sharedPrime)
print("    Publicly Shared Base:  ", sharedBase)

# Alice Sends Bob A = g^x mod n
A = (sharedBase ** aliceSecret) % sharedPrime
print("\n  Alice Sends Over Public Chanel: ", A)

# Bob Sends Alice B = g^y mod n
B = (sharedBase ** bobSecret) % sharedPrime
print("Bob Sends Over Public Chanel: ", B )

print("\n------------\n")
print("Privately Calculated Shared Secret:")
# Alice Computes Shared Secret: s = B^x mod n
aliceSharedSecret = (B ** aliceSecret) % sharedPrime
print("    Alice Shared Secret: ", aliceSharedSecret)

# Bob Computes Shared Secret: s = A^y mod n
bobSharedSecret = (A ** bobSecret) % sharedPrime
print("    Bob Shared Secret: ", bobSharedSecret)
