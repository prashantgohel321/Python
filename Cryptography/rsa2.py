import random
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime(min_val=1000, max_val=5000):
    while True:
        p = random.randint(min_val, max_val)
        if is_prime(p):
            return p

if __name__ == "__main__":
    print("--- RSA Key Generation, Encryption, and Decryption ---")

    # --- Step 1: Generate two distinct large prime numbers, p and q ---
    p = generate_prime()
    q = generate_prime()

    # Ensure p and q are not the same number.
    while p == q:
        q = generate_prime()

    print(f"1. Generated Primes:")
    print(f"   p = {p}")
    print(f"   q = {q}\n")

    # --- Step 2: Calculate n and phi(n) ---
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    print(f"2. Calculated n and phi(n):")
    print(f"   n (modulus) = p * q = {n}")
    print(f"   phi(n) (totient) = (p-1) * (q-1) = {phi_n}\n")
    
    # --- Step 3: Choose a public exponent 'e' ---
    # 'e' must be 1 < e < phi_n and gcd(e, phi_n) = 1 (coprime).
    # Common values are 3, 17, 65537. We'll find one automatically.
    
    e = random.randint(3, phi_n - 1)
    # Keep picking a new 'e' until it's coprime with phi_n.
    while math.gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n - 1)

    print(f"3. Public Key:")
    print(f"   e (public exponent) = {e}\n")

    # --- Step 4: Calculate the private exponent 'd' ---
    # 'd' is the modular multiplicative inverse of 'e' modulo phi_n.
    # d * e ≡ 1 (mod phi_n)
    # This is easily calculated using pow(e, -1, phi_n) in Python 3.8+
    
    d = pow(e, -1, phi_n)
    
    print(f"4. Private Key:")
    print(f"   d (private exponent) = {d}\n")
    
    # --- Step 5: Encryption ---
    message = input("Enter a single character to encrypt: ")
    
    # This script only encrypts the first character of the input.
    if len(message) > 1:
        print("Note: Only the first character will be encrypted.")
    
    first_char = message[0]
    
    # Convert the character to its ASCII integer representation.
    message_int = ord(first_char)
    print(f"\nOriginal Message Character: '{first_char}' (ASCII: {message_int})")
    
    # Encrypt: ciphertext = (message_int ^ e) mod n
    ciphertext = pow(message_int, e, n)
    print(f"Encrypted Message (Ciphertext): {ciphertext}\n")

    # --- Step 6: Decryption ---
    # Decrypt: decrypted_int = (ciphertext ^ d) mod n
    decrypted_int = pow(ciphertext, d, n)

    # Convert the decrypted integer back to a character.
    decrypted_char = chr(decrypted_int)
    print(f"Decrypted Integer: {decrypted_int}")
    print(f"Decrypted Message Character: '{decrypted_char}'")