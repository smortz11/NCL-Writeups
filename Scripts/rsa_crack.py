from math import gcd
from sympy import isprime

# Inputs
n = int(input("Enter the modulus (N): "))
e = int(input("Enter the public exponent (e): "))
c = int(input("Enter the cipher text (c): "))

# Step 1: Factor n (simple trial division for demonstration)
def factor_n(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return i, n // i
    return None, None

p, q = factor_n(n)
if not p or not q:
    print("Failed to factor n. Try a more advanced factoring method.")
    exit()

print(f"Factors found: p={p}, q={q}")

# Step 2: Compute Euler's totient
phi = (p-1)*(q-1)

# Step 3: Compute modular inverse of e (private key d)
def modinv(a, m):
    # Extended Euclidean Algorithm
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q*x0, x0
    return x1 + m0 if x1 < 0 else x1

d = modinv(e, phi)
print(f"Private key d={d}")

# Step 4: Decrypt ciphertext
m = pow(c, d, n)
print(f"Decrypted message: {m}")
